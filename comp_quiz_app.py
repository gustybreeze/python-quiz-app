import json
import random
import time


def load_questions(filename = "questions.json"):
    with open(filename, "r") as file:
        return json.load(file)
    
def ask_question(q, question_num, total_questions, time_limit = 15):
    print(f"\nQuestion {question_num}/{total_questions}: {q['question']}")
    print(f"(You have {time_limit} seconds to answer.)")

    start_time = time.time()
    try:
        user_answer = input("Your answer: ")
    except:
        user_answer = ""
    end_time = time.time()

    if (end_time - start_time) > time_limit:
        print("Time's up!")
        return False

    return evaluate_answer(user_answer, q["answer"]) 

def evaluate_answer(user_answer, correct_answer):
    return user_answer.strip().lower() == correct_answer.strip().lower()

def save_result(name, score, total):
    percentage = round((score/total) * 100, 2)
    with open("result.txt", "a") as f:
        f.write(f"{name} scored {score}/{total} ({percentage}%)\n")


def run_quiz():
    print("Welcome to the quiz!")
    name = input("Enter your name: ")
    questions = load_questions()
    random.shuffle(questions) 


    score = 0
    total = len(questions) 

    for i, q in enumerate(questions, start=1):
        if ask_question(q, i, total):
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! Correct answer was: {q['answer']}\n")

    percentage = round((score/total) * 100, 2)
    print(f"\n Quiz completed! {name}, you scored {score}/{total}")
    print(f"Percentage: {percentage}%")

    save_result(name, score, total)
    print("Result saved in result.txt.") 


if __name__ == "__main__":
    run_quiz() 

