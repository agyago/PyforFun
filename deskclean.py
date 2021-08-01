#! /usr/bin/python3

import datetime
from pathlib import Path
import sys
import shutil

cur_dir = sys.argv[1] if len(sys.argv) > 1 else '.'
myfile = Path(cur_dir)

extentionpaths = { '.png'  : 'Image',
                   '.PNG'  : 'Image',
                   '.jpg'  : 'Image',
                   '.JPG'  : 'Image',
                   '.jpeg' : 'Image',
                   '.gif'  : 'Image',
                   '.HEIC' : 'Image',
                   '.log'  : 'LogFile',
                   '.ini'  : 'ConfigFile',
                   '.conf' : 'ConfigFile',
                   '.json' : 'JSONFile',
                   '.docx' : 'Document',
                   '.doc'  : 'Document',
                   '.dot'  : 'Document',
                   '.xls'  : 'Excel',
                   '.xlsm' : 'Excel',
                   '.pptx' : 'Document',
                   '.xml'  :  'Document',
                   '.xlsx' : 'Excel',
                   '.txt'  : 'Document',
                   '.yaml' : 'Document',
                   '.yml'  : 'Document',
                   '.pdf'  : 'PDF',
                   '.mp4'  : 'Media',
                   '.mov'  : 'Media',
                   '.MOV'  : 'Media',
                   '.ics'  : 'CalInvite',
                   '.rpm'  : 'Package',
                   '.msi'  : 'Package',
                   '.deb'  : 'Package',
                   '.dmg'  : 'Package',
                   '.nupkg': 'Package',
                   '.msu'  : 'Package',
                   '.pkg'  : 'Package',
                   '.ISO'  : 'Package',
                   '.iso'  : 'Package',
                   '.java' : 'Package',
                   '.jnlp' : 'Package',
                   '.exe'  : 'Package',
                   '.EXE'  : 'Package',
                   '.pp'   : 'PuppetFile',
                   '.rb'   : 'RubyFile',
                   '.ps1'  : 'PowerShell',
                   '.sh'   : 'shellscripts',
                   '.app'  : 'Application',
                   '.crt'  : 'certificate',
                   '.cert' : 'certificate',
                   '.cer'  : 'certificate',
                   '.crl'  : 'certificate',
                   '.chain': 'certificate',
                   '.crl'  : 'certificate',
                   '.key'  : 'certificate',
                   '.pfx'  : 'certificate',
                   '.pem'  : 'certificate',
                   '.p12'  : 'certificate',
                   '.jass' : 'Secrets',
                   '.csv'  : 'Excel',
                   '.gz'   : 'archive',
                   '.zip'  : 'archive',
                   '.rar'  : 'archive',
                   '.tgz'  : 'archive',
                   '.tar'  : 'archive',
                   '.html' : 'HTML',
                   '.py'   : 'PythonFile',
                   ''      : 'Unknown',
                   '.pcap' : 'Unknown',
                   '.vce'  : 'Unknown',
                   '.list' : 'Unknown',
                   '.lck'  : 'Unknown',
                   '.rsf'  : 'Unknown',
                   '.crdownload': 'Unknown',
                   '.vpptoken'  : 'Unknown',
                   '.localized' : 'Unknown',
                   '.drawio'    : 'Unknown',
                   '.chman'     : 'Unknown',
                   '.itermcolors': 'Unknown'
                   }

def rename_file(file, subpath: Path):
    if Path(subpath / file.name).exists():
        increment = 0
        while True:
            increment += 1
            newname = subpath/ f'{file.stem}_{increment}{file.suffix}'
            if not newname.exists():
                return newname
    else:
        return subpath/file.name

def file_iter(myfile):
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
                subpath = rename_file(file, subpath=subpath)
                                 
                shutil.move(file,subpath)

if __name__ == '__main__':
   file_iter(myfile)