import subprocess
import os, time

print('''

  +-------------------------------------+

            __                .__     
    _______/  |______    _____|  |__  
    /  ___/\   __\__  \  /  ___/  |  \ 
    \___ \  |  |  / __ \_\___ \|   Y  \ 
    /____  > |__| (____  /____  >___|  /
        \/            \/     \/     \/ 
        
  +------------SamuelTheodore-----------+
''')


print("make sure you exitcute script using cmd")
print("script, image and zipped file must be in same directory.")

photoname = input("image name, with file extension. (example: photo.png): ")
photoname = (photoname) # saves photoname
exists = os.path.isfile('./'+(photoname)) # checks if photname exist
if exists: # if it exist
    print("file selected.")
else: # if file does not exits
    print("file does not exist.")
    time.sleep(1)
    exit()

print("make sure the files you want to hide are in a zipped folder.")

zipfolder = input("zipped folder name, with file extension, works with rar. (example: folder.zip): ")
zipfolder = (zipfolder)
exists = os.path.isfile('./'+(zipfolder)) # checks if zipfolder exist
if exists: # if it exist
    print("file selected.")
else: # if file does not exits
    print("file does not exist.")
    time.sleep(1)
    exit()

print("make the new image the same file extension as the original.")

newimagename = input("new image name, with extension. (example: hiddenphoto.png): ")
newimagename = (newimagename)

# This time it wont check if file exist because now we are making a file

os.system("copy /b " + (photoname)+ "+" +(zipfolder)+ " " + (newimagename) + "." ) # command that copies files

print("done.")
input() # to make the script not close