#! /usr/bin/python3

from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from deskclean import file_iter
from pathlib import Path
from time import sleep


myfile = Path("/Users/ayago/Desktop/testfolder")
class scan(FileSystemEventHandler):
    def on_modified(self, event):
        file_iter(myfile)

observer = Observer()
event_handler = scan()
observer.schedule(event_handler, myfile, recursive=True)
observer.start()

try:
    while True:
        sleep(60)
except KeyboardInterrupt:
    observer.stop()
observer.join()