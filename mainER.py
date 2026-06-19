from pydub import AudioSegment 
from pathlib import Path
from pydub.playback import play


def userInput():
    print('What do you want lucas to say')
    userText = input()
    userText = userText.lower()
    userInput = userText.split()
    return(userInput)
 
def getWordPath(word):
    basepath = str(Path(__file__).parent)
    folderPath = basepath + "/LucasSounds/"
    endingPath = ".mp3"
    outputPath = folderPath + word + endingPath
    outputPathPath = Path(outputPath)
    if outputPathPath.is_file():
        return(outputPath)
    else:
        print("we do not have the word " + word)
        

def getAudioSegment(word):
    return(AudioSegment.from_file(getWordPath(word), format="mp3"))

def exportPath(exportName):
    basepath = str(Path(__file__).parent)
    exportPath = basepath + "/outputs/" + exportName + ".mp3"

    exportPathPath = Path(exportPath)
    if exportPathPath.is_file():
        print("name already exists chose again -_-")
        while exportPathPath.is_file():
            print("new file name please")
            exportName = input()
            exportPath = basepath + "/outputs/" + exportName + ".mp3"
            exportPathPath = Path(exportPath)
        return(exportPath)
    else:
        return(exportPath)

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
    