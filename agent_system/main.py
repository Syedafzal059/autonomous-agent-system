from .planner import create_plan
from .executer import executer_plan
from .memory import Memory
from .critic import evaluate
from  config import MAX_RETRIES, SCORE_THRESHOLD

def run_agent(retries=0):
    memory = Memory()
    user_input = input("Enter your task:  ")
    
    #get memory context
    recent_memory = memory.get_recent()
    memory_context = str(recent_memory)    
    feedback = ""
    best_result= None
    best_score = -1
    for attempt in range(MAX_RETRIES):
        print(f"\n Attempt{attempt +1}")


        print("\n[PLANNER]")
        plan = create_plan(user_input, memory_context, feedback)
        print(plan)

        print("\n[EXECUTOR]")
        result = executer_plan(plan)
        print(result)

        print("\n[CRITIC]")
        evaluation = evaluate(user_input, plan, result)
        print(evaluation)

        score = evaluation.get("score", 0)
        feedback = evaluation.get("feedback", "")

        #track best
        if score > best_score:
            best_score = score
            best_result= result

        if score >= SCORE_THRESHOLD:
            print("\n GOOD ENOUGH!, stopping retries")
            break

    #store everything
    memory.add(user_input, plan, result)
    print("\n FINAL OUTPUT")
    print(best_result)


if __name__ =="__main__":
    run_agent()