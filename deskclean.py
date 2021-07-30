#! /usr/bin/python3

import datetime
from pathlib import Path
import shutil
import sys

cur_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
myfile = Path(cur_dir)

extentionpaths = { '.png': 'Image', '.jpg': 'Image','.docx': 'Document', '.rpm': 'Package'}
for file in myfile.iterdir():
   if file.is_file() and file.name != '.DS_Store':
       date = file.stat().st_mtime
       year = datetime.datetime.fromtimestamp(date).strftime("%Y")
       month = datetime.datetime.fromtimestamp(date).strftime("%B")
       rootpath= myfile.joinpath(extentionpaths[file.suffix])
       newpath = rootpath.joinpath(year)
       subpath = newpath.joinpath(month)
       if file.suffix in extentionpaths:
           if not rootpath.exists():
               rootpath.mkdir()
           if not newpath.exists():
               newpath.mkdir()
           if not subpath.exists():
               subpath.mkdir()
           shutil.move(file,subpath)
