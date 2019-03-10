path_name = "C:/Users/Owner/PycharmProjects/Memrize/Sonnets/Sonnet"
poem_lines = []
user_words = []


def tailorUserLine(userLine, poemLine):
    if len(userLine) < len(poemLine):
        missingLength = len(poemLine) - len(userLine)
        for i in range(0, missingLength):
            userLine.append("NULL")
        return userLine
    elif len(userLine) > len(poemLine):
        excessLength = len(userLine) - len(poemLine)
        for i in range(0, excessLength):
            del userLine[-1]
        return userLine
    else:
        return userLine


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
    #print(poem_words[i])

del poem_lines[0]
for poem_line in poem_lines:
    line = input('Please enter the next line: ')
    user_words = line.split(" ")

    user_words = tailorUserLine(user_words, poem_line)

    for i in range(len(user_words)):
        if user_words[i] == poem_line[i]:
            print("Correct")
        else:
            print("Mismatch")
            print("The user's next word is " + user_words[i])
            print("The poem's next word is " + poem_line[i])
