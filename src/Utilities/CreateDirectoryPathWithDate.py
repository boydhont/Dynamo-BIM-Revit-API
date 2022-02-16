import os
from datetime import datetime

date = datetime.today().strftime('%Y%m%d')[2:]
comment = "_" + IN[1].replace(" ", "_")
if comment == "_": comment = ""
OUT = os.path.join(IN[0], date + comment)
