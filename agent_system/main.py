from .planner import create_plan
from .executer import executer_plan


def run_agent():
    user_input = input("Enter your task:  ")
    print("\n[PLANNER]")
    plan = create_plan(user_input)
    print(plan)

    print("\n[EXECUTOR]")
    result = executer_plan(plan)
    print(result)


if __name__ =="__main__":
    run_agent()