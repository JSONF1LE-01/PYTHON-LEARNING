secret_Word = "giraffe"
guesses = ""
trys = 0
while guesses != secret_Word and trys <= 3:
     guesses = input("enter your guess: ")
     print("you have tryied " + str(trys) + " times")
     trys += 1
     if guesses == secret_Word:
          print("you win")
     elif guesses != secret_Word:
          print("you dont win ,this mf dont miss")

print("end")