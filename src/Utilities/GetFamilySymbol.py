import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetFamilySymbol(element):
    if element == None: return None
    familySymbol = element.Symbol
    if familySymbol == None: return None
    return familySymbol

element = IN[0]
OUT = GetFamilySymbol(element)