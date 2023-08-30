import random

userAnswers = []
correctAnswers = []
questionStrings = []

NUM_QUESTIONS = 10

for i in range(NUM_QUESTIONS):
    a = random.randint(0, 10)
    b = random.randint(0, 10)

    userAnswer = int(input(f'{a} * {b} = '))

    questionStrings.append(f'{a} * {b}')
    userAnswers.append(userAnswer)
    correctAnswers.append(a * b)

correctCount = 0
for i in range(NUM_QUESTIONS):
    if userAnswers[i] == correctAnswers[i]:
        print(f'Oikein :-) {questionStrings[i]} = {correctAnswers[i]}')
        correctCount += 1
    else:
        print(f'Väärin :-( Oikea vastaus on: {questionStrings[i]} = {correctAnswers[i]}')

print(f'Sait {correctCount}/{NUM_QUESTIONS} oikein!')