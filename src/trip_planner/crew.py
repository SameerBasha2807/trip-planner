from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent

from trip_planner.eval.evaluator import llm_evaluate
from trip_planner.eval.validator import validate_plan
from trip_planner.utils.metrics import Metrics

# ✅ CrewAI native Ollama LLM string
LLM = "ollama/llama3"


@CrewBase
class TripPlanner:
    """Trip planner crew."""

    agents: list[BaseAgent]
    tasks: list[Task]

    # ── AGENTS ──────────────────────────────────────────────────────────────

    @agent
    def travel_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["travel_researcher"],
            llm=LLM,
            verbose=True,
        )

    @agent
    def budget_planner(self) -> Agent:
        return Agent(
            config=self.agents_config["budget_planner"],
            llm=LLM,
            verbose=True,
        )

    @agent
    def itinerary_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["itinerary_generator"],
            llm=LLM,
            verbose=True,
        )

    @agent
    def local_expert(self) -> Agent:
        return Agent(
            config=self.agents_config["local_expert"],
            llm=LLM,
            verbose=True,
        )

    # ── TASKS ────────────────────────────────────────────────────────────────
    # Context chaining: each task receives the outputs of earlier tasks so
    # agents genuinely collaborate rather than working in isolation.
    #
    #   research  ──┐
    #               ├──► budget  ──┐
    #               │              ├──► itinerary  ──► local
    #               └──────────────┘
    #
    # NOTE: context must be a list of Task *objects* — YAML string references
    # are NOT supported by CrewAI, so this wiring is done here in Python.

    @task
    def research_task(self) -> Task:
        # First task — no prior context needed
        return Task(config=self.tasks_config["research_task"])

    @task
    def budget_task(self) -> Task:
        # Reads the researcher's findings to produce a realistic budget
        return Task(
            config=self.tasks_config["budget_task"],
            context=[self.research_task()],
        )

    @task
    def itinerary_task(self) -> Task:
        # Reads research + budget to build an itinerary that fits both
        return Task(
            config=self.tasks_config["itinerary_task"],
            context=[self.research_task(), self.budget_task()],
        )

    @task
    def local_task(self) -> Task:
        # Reads the full itinerary to weave in local tips naturally
        return Task(
            config=self.tasks_config["local_task"],
            context=[self.research_task(), self.itinerary_task()],
        )

    # ── CREW  ────────────────────────────────────────────────────────────────

    @crew
    def crew(self) -> Crew:
        """
        IMPORTANT: @crew MUST return a Crew instance — not a callable.
        Use TripPlanner().run(inputs) for execution with metrics/eval.
        """
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )

    # ── PUBLIC ENTRY POINT ───────────────────────────────────────────────────

    def run(self, inputs: dict) -> dict:
        """
        Execute the crew with the given inputs and return the plan plus metrics.

        Args:
            inputs: dict with keys 'destination', 'days', 'budget'

        Returns:
            {
              "output": str,
              "metrics": {
                  "latency": float,
                  "quality": dict,
                  "validation": dict,
                  "success": bool,
              }
            }
        """
        metrics = Metrics()

        result = self.crew().kickoff(inputs=inputs)
        output = str(result)

        evaluation = llm_evaluate(output, LLM)
        validation = validate_plan(output)

        success = (
            evaluation.get("score", 0) >= 7
            and validation.get("all_passed", False)
        )

        return {
            "output": output,
            "metrics": {
                "latency": metrics.total_latency(),
                "quality": evaluation,
                "validation": validation,
                "success": success,
            },
        }