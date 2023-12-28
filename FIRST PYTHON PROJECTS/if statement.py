is_male = True
is_tall = True

if is_male and is_tall :
    print("you are a male and tall")
elif is_male and not(is_tall):
    print("you are a male but you are not tall")
elif not(is_male) and is_tall:
    print("you are tall but not a male")
else:
    print("you are neither male or tall")