swears = open("swears.csv", "r")
key = swears.read()

split = key.split(",")
# print(split)

message = 'poop'


def bad_word_test():
    for word in split:
        if message == word:
            return True
    return False


if bad_word_test():
    print('bad word')
else:
    print("child of god")
