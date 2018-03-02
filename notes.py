
import json


class Notes:
    @classmethod
    def add_note(self, title, note):
        _id = 0
        idList=[]
        try:
            with open("Note.json", "r") as rf:
                    jsonobj = json.load(rf)
                    for i in jsonobj["notes"]:
                        idList.append(i)

                    nrList = len(idList)
                    _id = idList[(idList[nrList - 1])] + 1

        except FileNotFoundError as e:
            _id = 1
            print(e)

        with open("Note.json", "a") as wf:
            newJsonObject = {"Id": _id,
                             "Title": title,
                             "Note": note}
            json.dump(newJsonObject, wf)
        # TODO: Check if file exists
        # TODO: Get the highest id and add one as the new id for the note.
        # TODO: If there is no file: _id = 0
        # TODO: Add new note to file in json format
        # Exception, file not found error


    @classmethod
    def remove_note(self, _id):
        # TODO: Load file
        # TODO: Remove note with the given id.
        pass

    @classmethod
    def edit_note(self, _id, title, note):
        # TODO: Load file
        # TODO: Edit note with the given id.
        pass

    @classmethod
    def list_single_note(self, _id):
        # TODO: Load file
        # TODO: Display note with the given id.
        pass

    @classmethod
    def list_all_notes(self):
        # TODO: Load file
        # TODO: Show all the things!! \(^0^)/
        pass
