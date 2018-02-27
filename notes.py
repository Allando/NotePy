
import json


class Notes:
    def __init__(self):
        pass

    @staticmethod
    def add_note(title, note, time=None):
        _id = 0
        idList = []

        try:
            with open('notes.json', 'r') as rw:
                for i in rw:
                    for "Id" in i:
                        idList.append("Id")
                        r = idList[ len(idList) -1 ]
                        _id = r + 1
        except:
            _id = 0

with open('notes.json', 'a') as fw:
    if time == None:
        time = "na"

    note = {"Id": _id,
            "Title": title,
            "Note": note,
            "Notification time": time}

    fw.write(json.dump(note, fw))
fw.close()

def remove_note(self):
    pass

def edit_note(self):
    pass

