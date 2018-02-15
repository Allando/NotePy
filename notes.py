
import json


class Notes:
    def __init__(self):
        pass

    @staticmethod
    def add_note(title, note, time=None):
        with open('notes.json', 'a') as fw:
            if time == None:
                time = "na"
            
            note = {"Title": title,
                    "Note": note,
                    "Notification time": time}
   
            fw.write(json.dump(note, fw))
        fw.close()

    def remove_note(self):
        pass

    def edit_note(self):
        pass

