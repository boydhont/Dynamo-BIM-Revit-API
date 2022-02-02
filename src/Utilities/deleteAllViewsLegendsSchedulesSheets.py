import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getAllViews():
	filter = ElementCategoryFilter(BuiltInCategory.OST_Views)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getAllSheetsWithoutProjektInfo():
	filter = ElementCategoryFilter(BuiltInCategory.OST_Sheets)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	sheets = collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
	return [i for i in sheets if i.Name != 'Projektinfo']

def getAllSchedules():
	filter = ElementCategoryFilter(BuiltInCategory.OST_Schedules)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()


def getElementsToDelete(elements):
	elementsToDelete = []
	for element in elements:
		elementsToDelete.append(element.Id)
	return elementsToDelete

def flatten(t):
    return [item for sublist in t for item in sublist]

def deleteElements(elements):
	trans = Transaction(DocumentManager.Instance.CurrentDBDocument)
	trans.Start("Delete views, legends, views and sheets")
	for id in elements: 
		try:
			DocumentManager.Instance.CurrentDBDocument.Delete(id)
		except:
			continue
	trans.Commit()
	return str(elements.Count)

views = flatten([getAllViews(), getAllSheetsWithoutProjektInfo(), getAllSchedules()])
OUT = deleteElements(getElementsToDelete(views))