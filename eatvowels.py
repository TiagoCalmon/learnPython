# Prompt the user to enter a word
# and assign it to the userWord variable.
userWord = str(input("Type a word: "))
userWord = userWord.upper()
wordWithoutVovels = ""
for letter in userWord:
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        wordWithoutVovels += letter
        #print(letter)
print(wordWithoutVovels)

    # Complete the body of the for loop.