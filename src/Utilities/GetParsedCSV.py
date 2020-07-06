import clr
clr.AddReference("System.IO")
from System.IO import File
clr.AddReference("System.Text")
from System.Text import Encoding

def GetParsedCSV(filePath):
    try:
        parsedCSV = []
        lines = File.ReadAllLines(filePath) #Encoding is necessary for foreign characters
        for line in lines: parsedCSV.append(line.split(';'))
        return parsedCSV
    except:
        return None