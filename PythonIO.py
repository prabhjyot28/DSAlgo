#FILE

# Modes - w, r, r+, a
# W - write , R - read, r+ - Read and write , a - append
# Note when we are writing to a file it will remove everything that was previously there, so if you want to write in the end of an existing file use append mode.

myFile  = open("input.txt", mode)

# Some Properties on myFile that we can access.
print(myFile.name, myFile.mode)

# Write to a file.
myFile = open("input.txt", "w")
myFile.write("Hello,\nHope you are doing well!")
myFile.close()

# Read a file.
myFile = open("input.txt", "r")
print(myFile.read())  # Reads the whole FILE
# Hello,
# Hope you are doing well!

print(myFile.read(5))  # Then it will read only starting 5 characters of the file.
print(myFile.read(5))  # Then it will start reading next 5 characters (not as previously read) because of seek pointer.

# When ever we read or write a file we have a seek pointer that keeps track of where we are in the file.
# To reset  this seek pointer we can either run the seek function or close and reopen the file.
myFile.seek(0)  # It will set the seek pinter back to 0th position.


# Read one line of file at a time (Iteartiing through a file.)
myFile = open("input.txt", "r")
myFile.readLine()   # Reads one line at a time (NOTE - position of seek pointer moves)

for line in myFile:   # This way we can also readlines in files.
    print(line)










#----------------------------------------TEMP FILE MODULE------------------------------------------------------------------------------#

import tempfile   # to create a temporary file in python.
tf = tempfile.TemporaryFile()   # Create a temp file.

tf.write(b"Store some data")    # Note we only store bytes object in our temp file so we need to convert our string into byte object by writing b in front of it.
tf.seek(0)
print(tf.read())
tf.close()










#----------------------------------------ZIP FILE MODULE -------------------------------------------------------------------------------#

import zipfile    # to create a zipfile in python.

# Open and list
zip = zipfile.ZipFile("myzipfile.zip", "r")
print(zip.namelist())   # It will print the list of names of all files inside zip folder.

# Meta data in zip folder
for meta in zip.infolist():
    print(meta)

# Get meta data for particular file.
info  = zip.getinfo("file.txt")   # Get the meta data for file.txt inside zip folder

# Access to files inside zip folder.
print(zip.read("file.txt"))
    #---OR--#
with zip.open("file.txt") as f:
    print(f.read())

# Extracting files from zip folder.
zip.extract("file.txt")

# To extract all
zip.extractall()

#close the zip file.
zip.close()
