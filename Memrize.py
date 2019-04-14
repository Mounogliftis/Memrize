path_name = "C:/Users/Owner/PycharmProjects/Memrize/Sonnets/Sonnet"
poem_lines = []
user_words = []


def tailor_user_line(userline, poemline):
    if len(userline) < len(poemline):
        missing_length = len(poemline) - len(userline)
        for i in range(0, missing_length):
            userline.append("NULL")
        return userline
    elif len(userline) > len(poemline):
        excessLength = len(userline) - len(poemline)
        for i in range(0, excessLength):
            del userline[-1]
        return userline
    else:
        return userline


file = open(path_name + str(18) + '.txt', 'r')
poem = file.readlines()
for line in poem:
    poem_lines.append(line.split(" "))

poem_lines[13] = [word for word in poem_lines[13] if word not in ""]
poem_lines[14] = [word for word in poem_lines[14] if word not in ""]

for i in range(1, 15):
    temp_words = []
    for word in poem_lines[i]:
        word = word.strip("\n")
        temp_words.append(word)
    poem_lines[i] = temp_words
    # print(poem_words[i])

del poem_lines[0]
for poem_line in poem_lines:
    line = input('Please enter the next line: ')
    user_words = line.split(" ")

    user_words = tailor_user_line(user_words, poem_line)

    for i in range(len(user_words)):
        if user_words[i] == poem_line[i]:
            print("Correct")
        else:
            print("Mismatch")
            print("The user's next word is " + user_words[i])
            print("The poem's next word is " + poem_line[i])
