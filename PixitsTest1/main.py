from pydub import AudioSegment 
from pathlib import Path
from pydub.playback import play

#gather user input and return files / errors for missing words / also handle future setings logic (skip unkwnow words instead of error ect)
wordList = {
            "_space": "_space",
            "as": "as",
            "first": "first",
            "hell": "hell",
            "i'm": "i'm",
            "let's": "let's",
            "reason": "reason",
            "same": "same",
            "so": "so",
            "started": "started",
            "then": "then",
            "things": "things",
            "tired": "tired",
            "uh": "uh",
            "well": "well"
            }


def wordPath(word):
    script_dir = str(Path(__file__).parent)
    basePath=script_dir+"/LucasSounds/"
    endingPath=".mp3"

    curPath=basePath+"_space"+endingPath
    return(curPath)


def userInput():
    print('What do you want lucas to say')
    userText = input()
    userInput = userText.split()
    exportFile(processAudio(userInput,wordList))

def processText(userInput, wordList):
    for x in userInput:
        if x in wordList:
            print(wordList[x])
        else:
            print("Nope")

def processAudio(userInput,wordList):
    outputSound = AudioSegment.from_file(wordPath("_space"), format="mp3")
    for word in userInput:
        if word in wordList:
            outputSound += AudioSegment.from_file(wordPath(word), format="mp3")
        else:
            raise ValueError("Word not in dictionary")
    return(outputSound)

def exportFile(soundOutput):
    script_dir = str(Path(__file__).parent)
    print("got here")

    outputPath=script_dir+"/outputs/"+"lucasOutput4.mp3"
    soundOutput.export(outputPath, format="mp3")

userInput()
#C:\Users\Rain\Desktop\personal proj\LucasSaysProject\LucasSounds\_space.mp3