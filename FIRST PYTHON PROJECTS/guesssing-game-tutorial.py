secret_word = "Girrafe"
guess =""
guess_count = 0
guess_limit = 3
out_of_guessse = False

while guess != secret_word and not (out_of_guessse):
    if guess_count < guess_limit:
        guess = input("your guess: ")
        guess_count += 1
    else :
         out_of_guessse = True
if out_of_guessse:
    print("OUT OF GUESSES!! you loose")
else:
    print("you win")