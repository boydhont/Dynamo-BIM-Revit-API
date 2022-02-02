import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getAllRevitLinkInstance():
	filter = ElementClassFilter(RevitLinkInstance)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
	
def getAllRevitLinkType():
	filter = ElementClassFilter(RevitLinkType)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()
	
def getAllImportInstance():
	filter = ElementClassFilter(ImportInstance)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getAllRasterImages():
	filter = ElementCategoryFilter(BuiltInCategory.OST_RasterImages)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getAllImageInstance():
	filter = ElementClassFilter(ImageInstance)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getAllImageType():
	filter = ElementClassFilter(ImageType)
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

views = flatten([getAllRevitLinkInstance(), getAllRevitLinkType(), getAllImportInstance(), getAllRasterImages(), getAllImageInstance(), getAllImageType()])
OUT = deleteElements(getElementsToDelete(views))