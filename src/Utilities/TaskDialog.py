import clr
clr.AddReference("RevitAPIUI")
from Autodesk.Revit.UI import TaskDialog

title = str(IN[0])
message = str(IN[1])

OUT = TaskDialog.Show(title, message)