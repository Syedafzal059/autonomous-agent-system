from .utils.llm import call_llm 

def create_plan(user_input: str) -> str:
    prompt = f"""
    Break the following task into clear step-by-step plan.and

    Task:
    {user_input}

    Output Only steps.
    """

    return call_llm(prompt)


    