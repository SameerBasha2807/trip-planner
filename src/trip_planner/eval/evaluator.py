from langchain_ollama import ChatOllama
import json
import re

def llm_evaluate(output: str, model_name: str) -> dict:

    # 🔥 build LLM inside evaluator
    llm = ChatOllama(
        model=model_name.replace("ollama/", ""),
        temperature=0
    )

    prompt = f"""
    Evaluate this travel plan:

    {output}

    Score from 1–10:
    1. Completeness
    2. Realism
    3. Personalization
    4. Clarity

    Return ONLY JSON:
    {{
        "completeness": number,
        "realism": number,
        "personalization": number,
        "clarity": number,
        "score": number
    }}
    """

    try:
        response = llm.invoke(prompt)

        text = getattr(response, "content", str(response))

        match = re.search(r"\{.*\}", text, re.DOTALL)
        if match:
            return json.loads(match.group())

    except Exception as e:
        print("Evaluation error:", e)

    return {
        "completeness": 5,
        "realism": 5,
        "personalization": 5,
        "clarity": 5,
        "score": 5
    }