from question import Question_class

Question_Prompts = [
    "What color are apples? \n(a) red/green\n (b) purple\n (c)orange\n\n",
    "What color are bananas? \n(a) Teal\n(b) Magenta\n(c) yellow\n\n",
    "what color are strawberries? \n(a) yellow\n(b) Red\n(c) Blue\n\n"
]
Questions = [
    Question_class(Question_Prompts[0], "a"),
    Question_class(Question_Prompts[1], "c"),
    Question_class(Question_Prompts[2], "b")
]

def run_test(Questions):
    score = 0
    for Question in Questions:
        answer = input(Question.prompt)
        if answer == Question.answer:
            score += 1
    print("you got " + str(score) + "/" + str(len(Questions)) + " correct")


run_test(Questions)