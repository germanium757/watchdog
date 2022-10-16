import time
from watchdog.observers import Observer
from shedule_class import FileSchedule

path_to_file = "./files"
event_handler = FileSchedule(path_to_file)
observer = Observer()
observer.schedule(event_handler, path=path_to_file, recursive=True)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
