from openai.resources.completions import CompletionsWithStreamingResponse
from typing_extensions import evaluate_forward_ref
from .utils.llm import call_llm
import json

def evaluate(user_input: str, plan:str, result:str) -> dict:
    prompt = f"""
    You are a strict evaluator.

    Task:
    {user_input}

    Plan:
    {plan}

    Result:
    {result}

    Evaluate based on:
    -correctness
    -completeness
    -relevence

    Output JSON ONLY:
    {{
        "score":(0,10),
        "feedback": "What is wrong or missing"
    }}"""

    response = call_llm(prompt)

    try:  
        return json.loads(response)
    except:
        return {
            "score": 5,
            "feedback": "Failed to parse evaluation"
        }