from re import S
from .utils.llm import call_llm
from .tools.calculator import CalculatorTool
from .tools.search import SearchTool


tools = {
    "calculator": CalculatorTool(),
    "search": SearchTool()
}


def decide_tool(step:str)-> str:
    prompt = f"""
    Decide which tool to use for the step below.

    Available tools:
    - calculator
    - search

    Steps:
    {step}

    Output ONLY tool name.
    """
    return call_llm(prompt).strip().lower()


def executer_plan(plan: str) -> str:
    steps = plan.split("\n")
    results = []

    for step in steps:
        if not step.strip():
            continue
        tool_name = decide_tool(step)
        tool = tools.get(tool_name)

        if tool:
            output = tool.run(step)
        else:
            output = f"No tool found for step: {step}"
        results.append(f"{step} -> {output}")

    return "\n".join(results)