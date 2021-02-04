import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import TaskDialog
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getAllElements():
	filter = ElementClassFilter(LinePatternElement)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getElementsToDelete(elements):
	elementsToDelete = []
	for element in elements:
		if element.GetLinePattern().Name.StartsWith("IMPORT-") == False: continue
		elementsToDelete.append(element.Id)
	return elementsToDelete

def deleteElements(elements):
	trans = Transaction(DocumentManager.Instance.CurrentDBDocument)
	trans.Start("Delete line patterns from DWGs")
	for id in elements: DocumentManager.Instance.CurrentDBDocument.Delete(id)
	trans.Commit()
	return str(elements.Count)

message = deleteElements(getElementsToDelete(getAllElements())) + " line patterns from imported DWGs have been deleted"
TaskDialog.Show("Succes", message)
OUT = message

#OUT = getAllElements()[0].GetLinePattern().Name.StartsWith("IMPORT-")