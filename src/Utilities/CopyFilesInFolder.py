import os
import shutil

def getFiles(filePath):
	files = []
	for file in os.listdir(filePath):
		if file.endswith(IN[2]) == False: continue #IN[2] = file extension as string
		files.append(file)
	return files

for file in getFiles(IN[1]): shutil.copyfile(os.path.join(IN[1], file), os.path.join(IN[0], file))
OUT = IN[0]
