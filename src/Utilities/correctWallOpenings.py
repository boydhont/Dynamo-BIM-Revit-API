import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getFamilyInstances():
	filter = ElementClassFilter(FamilyInstance)
	collector = FilteredElementCollector(DocumentManager.Instance.CurrentDBDocument)
	return collector.WherePasses(filter).WhereElementIsNotElementType().ToElements()

def getOpenings(familyInstances):
	openings = []
	for familyInstance in familyInstances:
		if not familyInstance.Symbol.FamilyName.startswith("Allg_") : continue
		if familyInstance.LookupParameter("Ebenenhöhe über 00") == None : continue
		openings.append(familyInstance)
	return openings
	
def correctOpenings(openings):
	trans = Transaction(DocumentManager.Instance.CurrentDBDocument)
	trans.Start("Höhenangaben Wanddurchbrüche korrigieren")
	
	for opening in openings:
		opening.LookupParameter("Ebenenhöhe über 00").Set(opening.Document.GetElement(opening.LevelId).Elevation)
		if opening.LookupParameter("UK über Ebene") != None and opening.LookupParameter("Achse über Ebene") != None : continue
		if opening.LookupParameter("Höhe von Ebene") == None : continue
		if opening.LookupParameter("UK über Ebene") != None :  opening.LookupParameter("UK über Ebene").Set(opening.LookupParameter("UK über Ebene").AsDouble() + opening.LookupParameter("Höhe von Ebene").AsDouble())
		if opening.LookupParameter("Achse über Ebene") != None : opening.LookupParameter("Achse über Ebene").Set(opening.LookupParameter("Achse über Ebene").AsDouble() + opening.LookupParameter("Höhe von Ebene").AsDouble());
		opening.LookupParameter("Höhe von Ebene").Set(0);
	
	trans.Commit()
	
	return openings

OUT = correctOpenings(getOpenings(getFamilyInstances()))