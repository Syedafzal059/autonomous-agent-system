from .utils.llm import call_llm 

def create_plan(user_input: str, memory_context: str= " ") -> str:
    prompt = f"""
    Break the following task into clear step-by-step plan.and

    Previous context:
    {memory_context}
    
    Task:
    {user_input}

    Output Only steps.
    """

    return call_llm(prompt)


    