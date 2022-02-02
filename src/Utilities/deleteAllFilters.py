import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getAllElements():
	filter = ElementClassFilter(ParameterFilterElement)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getElementsToDelete(elements):
	elementsToDelete = []
	for element in elements:
		elementsToDelete.append(element.Id)
	return elementsToDelete

def deleteElements(elements):
	trans = Transaction(DocumentManager.Instance.CurrentDBDocument)
	trans.Start("Delete Filter elements")
	for id in elements: DocumentManager.Instance.CurrentDBDocument.Delete(id)
	trans.Commit()
	return str(elements.Count)

message = deleteElements(getElementsToDelete(getAllElements())) + " Filters have been deleted"
OUT = message