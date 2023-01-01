QUESTIONS = {
    "Color of banana is YELLOW": [
        "True","False"
    ],
     "Color of Apple is RED": [
        "True","False"
    ],
     "Color of Mango is YELLOW": [
        "True","False"
    ],
     "Color of Grapes is GREEN/BLACK": [
        "True","False"
    ],
     "Color of Strawberry is RED": [
        "True","False"
    ]
}
s = 0
for question, alternatives in QUESTIONS.items():
    correct_answer = alternatives[0]
    for alternative in sorted(alternatives):
        print(f"  - {alternative}")

    answer = input(f"{question}? ")
    if answer == correct_answer:
        print("Correct!")
        s = s +1
        print('your score is :',s)
    else:
        print(f"The answer is {correct_answer!r}, not {answer!r}")

