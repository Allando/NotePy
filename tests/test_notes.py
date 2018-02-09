#!/bin/python

# Standard library
import unittest


class test_notes(unittest.TestCase):
    def test_add_note(self):
        self.assertEqual(notes.add_note('Message test', 'hello, there'), True)
        self.assertEqual(notes.add_note('A message to bob', ''), True)
        self.assertEqual(notes.add_note('', 'ayy'), False)
        self.assertEqual(notes.add_note('', ''), False)

    def test_remove_note(self):
        self.assertEqual(notes.remove_note('1'), True)
        self.assertEqual(notes.remove_note('999'), False)
        self.assertEqual(notes.remove_note('-1'), False)
        self.assertEqual(notes.remove_note('1.0'), False)

    def test_edit_note(self):
        self.assertEqual(notes.add_note(2, 'New Message test', 'Good bye'), True)
        self.assertEqual(notes.add_note(2, 'A message from alice', ''), True)
        self.assertEqual(notes.add_note(2, '', 'way'), False)
        self.assertEqual(notes.add_note(2, '', ''), False)

if __name__ == '__main__':
    unittest.main()

