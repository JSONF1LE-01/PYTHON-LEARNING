def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = tranlsation + "g"
        else:
            tranlsation = translation + letter
    return tranlsation
print(translate(input("Enter a phrase: ")))
'''
Multiline comments
'''
