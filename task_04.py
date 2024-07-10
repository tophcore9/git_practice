def checkio(words: str) -> bool:
    words_list = words.split()
    for i in range(len(words_list) - 2):
        if words_list[i].isalpha() and words_list[i+1].isalpha() and words_list[i+2].isalpha():
            return True
    return False


print("Example:")
print(checkio("Hello World hello"))

# These "asserts" are used for self-checking
assert checkio("Hello World hello") == True
assert checkio("He is 123 man") == False
assert checkio("1 2 3 4") == False
assert checkio("bla bla bla bla") == True
assert checkio("Hi") == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
