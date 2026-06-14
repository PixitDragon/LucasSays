#gather user input and return files / errors for missing words / also handle future setings logic (skip unkwnow words instead of error ect)
wordList = {
            "test": "test",
            "time": "time",
            "furries": "furries.mp3",
            "pixit": "pixit.mp3",
            }


def userInput():
    print('What do you want lucas to say')
    userText = input()
    userInput = userText.split()
    processText(userInput,wordList)

def processText(userInput, wordList):
    for x in userInput:
        if x in wordList:
            print(wordList[x])
        else:
            print("Nope")

userInput()
