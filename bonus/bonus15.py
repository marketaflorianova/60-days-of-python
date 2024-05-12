import json

with open("questions.json", 'r') as file:
    content = file.read()

data = json.loads(content)

score = 0
for question in data:
    print(question["question_text"])
    for index, alternative in enumerate(question["alternatives"]):
        print(index+1, alternative)
    user_choice = int(input("Enter your answer: "))
    question["user_choice"] = user_choice

    message = f"Your answer is {question['user_choice']}, " \
              f"Correct answer is {question['correct_answer']}"
    print(message)

    if question["user_choice"] == question["correct_answer"]:
        score = score +1

print(f"Score is ", score, "/", len(data))
