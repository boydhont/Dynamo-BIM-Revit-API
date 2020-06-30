import clr
clr.AddReference("System.Diagnostics.Process")
from System.Diagnostics import Process

def openURL(url):
	Process.Start(url)

url = IN[0]
OUT = openURL(url)