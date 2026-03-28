quiz = {
    "Capital of France": "paris",
    "Capital of Japan": "tokyo",
    "Capital of Cambodia": "phnom penh",
    "Capital of Thailand": "bangkok"
}

score = 0
for question in quiz:
    user_answer = input(question + ": ")
    if user_answer.strip().lower() == quiz[question]:
        print("Correct!")
        score += 1
    else:
        print("Wrong! Correct answer is:", quiz[question])

print("Your final score:", score, "/", len(quiz))