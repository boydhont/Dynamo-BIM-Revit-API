import clr
clr.AddReference('ProtoGeometry')
from Autodesk.DesignScript.Geometry import *
clr.AddReference("RevitAPI")
from Autodesk.Revit.DB import *
clr.AddReference("RevitNodes")
import Revit
clr.ImportExtensions(Revit.Elements)

def GetParameterValue(parameter):
	try:
		if parameter.StorageType == StorageType.Integer : return parameter.AsInteger()
		if parameter.StorageType == StorageType.Double : 
			if parameter.AsValueString() == None: return parameter.AsDouble()
			else : return parameter.AsValueString()
		if parameter.StorageType == StorageType.String : return parameter.AsString()
		if parameter.StorageType == StorageType.ElementId : return parameter.AsElementId()	
		return None		
	except:
		return None

def GetInstanceParameters(element, parameterNames):
	parameters = []
	for parameterName in parameterNames:
		try:
			parameters.append(element.LookupParameter(parameterName))
		except: continue
	return parameters

def GetFamilySymbolParameters(familyInstance, parameterNames):
	try:
		familySymbol = familyInstance.Symbol
		return GetInstanceParameters(familySymbol, parameterNames)
	except:
		return None
		
def GetWallTypeParameters(wall, parameterNames):
	try:
		wallType = wall.WallType
		return GetInstanceParameters(wallType, parameterNames)
	except:
		return None
	
def GetMergedParameterList(parameterLists):
	if len(parameterLists) == 0 : return None
	mergedParameterList = parameterLists[0]
	for parameterList in parameterLists:
		if parameterList == None : continue
		for i in range(0, len(parameterList)):
			parameter = parameterList[i]
			if parameter == None: continue
			mergedParameterList[i] = parameter
	return mergedParameterList
	
def GetParameterValues(parameterList):
	if parameterList == None: return None
	parameterValues = []
	for parameter in parameterList:
		parameterValues.append(GetParameterValue(parameter))
	return parameterValues
	
def GetNameStringFromValues(parameterValues):
	name = ""	
	if parameterValues == None: return None
	for value in parameterValues:
		if value == None: continue
		name += " - " + str(value)
	if len(name) >= 3 : name = name[3:len(name)]
	return name			
	
element = UnwrapElement(IN[0])
parameterNames = IN[1]

parameterLists = []
parameterLists.append(GetInstanceParameters(element, parameterNames))
parameterLists.append(GetFamilySymbolParameters(element, parameterNames))
parameterLists.append(GetWallTypeParameters(element, parameterNames))

parameterList = GetMergedParameterList(parameterLists)

parameterValues = GetParameterValues(parameterList)

OUT = GetNameStringFromValues(parameterValues)