import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getAllElements():
	filter = ElementClassFilter(LinePatternElement)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()