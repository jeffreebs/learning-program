def print_letters(strings):
    upper= 0
    lower = 0

    for letter in strings:
        if letter.isupper():
            upper+=1
        elif letter.islower():
            lower += 1
    print (f"The text have : {upper} upper letters")
    print (f"The text have : {lower} lower letters")

print_letters("Hello world from python")