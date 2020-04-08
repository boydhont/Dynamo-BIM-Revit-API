filePath = IN[0]

with open (filePath, "r") as inputFile:
    stringArray = inputFile.readlines()
    
OUT = stringArray