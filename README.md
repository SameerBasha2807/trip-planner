# TripPlanner Crew

An AI-powered multi-agent travel planning system built with **CrewAI** and Python. TripPlanner uses specialized AI agents to research, validate, and generate personalized travel plans based on user preferences.

## Features

* Multi-agent AI travel planning
* Personalized itinerary generation
* User preference-based recommendations
* Agent-based research and planning
* Custom evaluation and validation utilities
* Configurable agents and tasks using YAML
* Metrics and evaluation support
* CLI-based execution

## Tech Stack

* **Python 3.10 – 3.13**
* **CrewAI** — Multi-agent orchestration
* **UV** — Dependency and environment management
* **YAML** — Agent and task configuration
* **OpenAI API** — LLM-powered agents

## Project Structure

```text
trip_planner/
│
├── app.py
├── README.md
├── AGENTS.md
├── pyproject.toml
├── report.md
│
├── knowledge/
│   └── user_preference.txt
│
└── src/
    └── trip_planner/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        │
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        │
        ├── eval/
        │   ├── evaluator.py
        │   └── validator.py
        │
        ├── tools/
        │   └── custom_tool.py
        │
        └── utils/
            └── metrics.py
```

## How It Works

TripPlanner follows a multi-agent workflow where different AI agents collaborate to produce a travel plan.

```text
User Preferences
       │
       ▼
┌─────────────────────┐
│   AI Travel Agents  │
└──────────┬──────────┘
           │
           ▼
   Research & Planning
           │
           ▼
   Validation & Evaluation
           │
           ▼
   Personalized Itinerary
```

The agents and their responsibilities are configured in:

```text
src/trip_planner/config/agents.yaml
```

Tasks are defined in:

```text
src/trip_planner/config/tasks.yaml
```

The CrewAI workflow is implemented in:

```text
src/trip_planner/crew.py
```

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/SameerBasha2807/trip-planner.git
cd trip-planner
```

### 2. Create a virtual environment

Using Python:

```bash
python -m venv .venv
```

Activate it on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

### 3. Install UV

```bash
pip install uv
```

### 4. Install dependencies

```bash
crewai install
```

If required, dependencies can also be installed using:

```bash
uv sync
```

## Environment Variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
```

Do **not** commit your `.env` file or expose API keys publicly.

The `.gitignore` file is configured to prevent environment files and other sensitive/local files from being committed.

## Running the Project

From the project root:

```bash
crewai run
```

The application will initialize the configured CrewAI agents and execute the defined tasks.

The generated output can be written to:

```text
report.md
```

## Configuration

### Agents

Define and customize AI agents in:

```text
src/trip_planner/config/agents.yaml
```

You can configure properties such as:

* Role
* Goal
* Backstory
* LLM configuration
* Tools

### Tasks

Define agent tasks in:

```text
src/trip_planner/config/tasks.yaml
```

Tasks determine what each agent needs to accomplish and how the agents collaborate.

### Crew Logic

The main CrewAI workflow is implemented in:

```text
src/trip_planner/crew.py
```

This is where agents, tasks, tools, and execution flow are assembled.

## Evaluation

TripPlanner includes evaluation and validation utilities:

```text
src/trip_planner/eval/
```

These components can be used to evaluate generated travel plans and validate the quality of the output.

Metrics and supporting utilities are available under:

```text
src/trip_planner/utils/
```

## Customization

You can extend the project by:

1. Adding new AI agents.
2. Creating additional travel-planning tasks.
3. Adding custom tools.
4. Updating user preference inputs.
5. Adding new validation rules.
6. Creating additional evaluation metrics.
7. Integrating external APIs or data sources.

Custom tools can be added under:

```text
src/trip_planner/tools/
```

## Example Use Case

A user can provide preferences such as:

```text
Destination: Manali
Duration: 5 days
Budget: ₹30,000
Travel style: Adventure
Interests: Mountains, trekking, local food
```

The AI agents can use these preferences to construct a personalized travel itinerary containing destinations, activities, recommendations, and a structured travel plan.

## Development

Run the project from the root directory:

```bash
crewai run
```

For development, modify the agent configuration, task definitions, tools, or CrewAI workflow and run the project again.

## Security

Never commit sensitive credentials to GitHub.

Keep API keys in environment variables:

```env
OPENAI_API_KEY=your_key_here
```

The following files should remain local:

```text
.env
.env.local
.venv/
```

## License

This project is intended for educational and development purposes.

## Author

**Sameer Basha Achukatla**

GitHub: [SameerBasha2807](https://github.com/SameerBasha2807)
