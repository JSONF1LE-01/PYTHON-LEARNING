for letter in "Girraffe":
    print(letter)

#range(3, 10)

Friends = ["Felipe","Alex","Steven","Keyla","Mico","David","Toyita",]

for Friend in Friends:
    print(Friend)

for index in range(len(Friends)):
    print(index, Friends[index])
    if index == 0:
        print("first iteration")
    else:
        print("not first")