
import json


class Notes:
    @classmethod
    def add_note(self, title, note):
        # TODO: Check if file exists
        # TODO: Get the highest id and add one as the new id for the note.
        # TODO: If there is no file: _id = 0
        # TODO: Add new note to file in json format
        pass

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
