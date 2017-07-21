import os

def rename_files():
 file_list=os.listdir(r"/home/raghvendra/Desktop/prank/prank")
 #print(file_list)
 os.chdir(r"/home/raghvendra/Desktop/prank/prank")
 directory=os.getcwd()
 print("current working directory is"+directory)
 for file_name in file_list:
    print("OldName-"+file_name)
    print("NewName-"+file_name.translate(None,"0123456789")) 
    os.rename(file_name,file_name.translate(None,"0123456789"))
 os.chdir(r"/home/raghvendra/Desktop/prank/prank")

rename_files()