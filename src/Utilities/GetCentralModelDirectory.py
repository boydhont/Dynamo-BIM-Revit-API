import os
import clr
clr.AddReference('RevitAPI')
import Autodesk
from Autodesk.Revit.DB import ModelPathUtils
clr.AddReference('RevitServices')
import RevitServices
from RevitServices.Persistence import DocumentManager

doc = DocumentManager.Instance.CurrentDBDocument
cen = doc.GetWorksharingCentralModelPath()
OUT = os.path.dirname(ModelPathUtils.ConvertModelPathToUserVisiblePath(cen))
