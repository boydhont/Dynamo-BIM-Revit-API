import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getAllElements(): 
	document = DocumentManager.Instance.CurrentDBDocument
	filter = ElementLevelFilter(ElementId(-1),True)
	return FilteredElementCollector(document).WherePasses(filter).WhereElementIsNotElementType().ToElements()

OUT = getAllElements()