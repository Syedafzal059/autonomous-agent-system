from .planner import create_plan
from .executer import executer_plan
from .memory import Memory


def run_agent():
    memory = Memory()

    user_input = input("Enter your task:  ")
    
    #get memory context
    recent_memory = memory.get_recent()
    memory_context = str(recent_memory)    
    
    print("\n[PLANNER]")
    plan = create_plan(user_input, memory_context)
    print(plan)

    print("\n[EXECUTOR]")
    result = executer_plan(plan)
    print(result)


if __name__ =="__main__":
    run_agent()