import urllib

def read_file():
  file=open("/home/raghvendra/Desktop/Dropped Text.txt")
  content=file.read()
  file.close()
  speech(content)
  
def speech(content):
 connection=urllib.open("https://api.ispeech.org/api/rest?action=convert&text=content&voice=usenglishfemale &format=mp3 &frequency=44100 &bitrate=128&speed=1&startpadding=1 &endpadding=1 &pitch=110 &filename=myaudiofile")
 output=connection.read()
 print(output)

read_file()