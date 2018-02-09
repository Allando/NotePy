
import time


class NoteModel:
    def __init__(self, title, note, notify_time):
        self.title = title
        self.note = note
        self.n_time = notify_time
        self.c_time = asctime(time.localtime(time.time()))   

    
    
