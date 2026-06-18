from pydub import AudioSegment 
from pathlib import Path
from pydub.playback import play

def userInput():
    print('What do you want lucas to say')
    userText = input()
    userInput = userText.split()
    return(userInput)

def getWordPath(word):
    basepath = str(Path(__file__).parent)
    folderPath = basepath + "/LucasSounds/"
    endingPath = ".mp3"
    return(folderPath + word + endingPath)

def getAudioSegment(word):
    return(AudioSegment.from_file(getWordPath(word), format="mp3"))

def exportPath(exportName):
    basepath = str(Path(__file__).parent)
    return(basepath + "/outputs/" + exportName + ".mp3")

def exportThatStuff(fullAudio):
    print("what should the file be called?")
    exportName = input()
    fullAudio.export(exportPath(exportName), format="mp3")

def allTheStuff():
    wordArray = userInput()

    fullAudio = getAudioSegment("_space")

    for word in wordArray:
        fullAudio += getAudioSegment(word)
        
    exportThatStuff(fullAudio)

allTheStuff()
    