from .utils.llm import call_llm 

def create_plan(user_input: str, memory_context: str= " ", feedback: str= " ") ->  str:
    prompt = f"""
    Break the following task into clear step-by-step plan.and

    Previous context:
    {memory_context}

    Feedback from previous attempt:
    {feedback}
    
    Task:
    {user_input}

    Improve the plan if feedback suggests issues.

    Output Only steps-by-step plan.
    """

    return call_llm(prompt)


    