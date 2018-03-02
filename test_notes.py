#!/bin/python

# Standard library
import unittest

from notes import Notes


class test_notes(unittest.TestCase):
    def test_add_note(self):
        # Title - Note limitations
        self.assertEqual(Notes.add_note('Message test', 'hello, there'), True)
        self.assertEqual(Notes.add_note('A message to bob', ''), True)
        self.assertEqual(Notes.add_note('', 'ayy'), False)
        self.assertEqual(Notes.add_note('', ''), False)

        # File handling
        with self.assertRaises(FileNotFoundError):
            open('failtest.json', 'r')
        with self.assertRaises(FileNotFoundError):
            open('', 'r')

    def test_remove_note(self):
        self.assertEqual(Notes.remove_note('1'), True)
        self.assertEqual(Notes.remove_note('999'), False)
        self.assertEqual(Notes.remove_note('-1'), False)
        self.assertEqual(Notes.remove_note('1.0'), False)

    def test_edit_note(self):
        self.assertEqual(Notes.edit_note(2, 'New Message test', 'Good bye'), True)
        self.assertEqual(Notes.edit_note(2, 'A message from alice', ''), True)
        self.assertEqual(Notes.edit_note(2, '', 'way'), False)
        self.assertEqual(Notes.edit_note(2, '', ''), False)


if __name__ == '__main__':
    unittest.main()
