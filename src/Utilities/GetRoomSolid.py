import clr
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitServices")
from RevitServices.Persistence import DocumentManager
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def getRoomSolid(room):
	if(room == None): return None
	return SpatialElementGeometryCalculator(room.Document).CalculateSpatialElementGeometry(room).GetGeometry()

room = UnwrapElement(IN[0])
OUT = getRoomSolid(room)