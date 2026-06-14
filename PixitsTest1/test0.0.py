from pydub import AudioSegment 
from pathlib import Path
from pydub.playback import play

# 1. Get the directory of the current script
script_dir = str(Path(__file__).parent)

goingPath=script_dir+"/testSounds/going.mp3"

testSound=AudioSegment.from_file("/Users/pixitt/Documents/GitHub/LucasSays/PixitsTest1/test.mp3", format="mp3")
goingSound=AudioSegment.from_file(goingPath, format="mp3")
soundSound=AudioSegment.from_file("/Users/pixitt/Documents/GitHub/LucasSays/PixitsTest1/testSounds/sound.mp3", format="mp3")

combined = testSound + goingSound + soundSound

# simple export
file_handle = combined.export("./output2.mp3", format="mp3")







sentence=input()
formatted=sentence.split()
sentence=formatted

basePath=script_dir+"/LucasSounds/"
endingPath=".mp3"

curPath=basePath+"_space"+endingPath
curSound=AudioSegment.from_file(curPath, format="mp3")
combined2=curSound

for word in sentence:
    curPath=basePath+word+endingPath
    curSound=AudioSegment.from_file(curPath, format="mp3")
    combined2+=curSound

curPath=basePath+"lucasOutput3.mp3"
file_handle = combined2.export(curPath, format="mp3")


# Load your audio file (works for MP3, WAV, etc.)
sound = AudioSegment.from_file(curPath, format="mp3")

# Play the audio file out loud
play(sound)