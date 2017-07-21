import urllib

def read_text():
	quotes=open("/home/raghvendra/Desktop/Dropped Text.txt")
	content_of_file=quotes.read()
	print(content_of_file)
	quotes.close()
	chec_profanity(content_of_file)


def chec_profanity(text_to_check):
  connection=urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
  output=connection.read()
  #print(output)
  connection.close()
  if "true" in output:
  	print("profanity alert")
  elif "false" in output:
   print("This document has no curse words")
  else:
    print("Document is not scanned properly")  

read_text()