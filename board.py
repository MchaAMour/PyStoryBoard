from note import Note


class Board:
    def __init__(self):
        #self.boardId = ay7agarandom
        self.notesList = []

    def addNote(self, note):
        if not self.checkNoteExists(note):
            self.notesList.append(note)
        else:
            print("Note Already Exists")

    def deleteNote(self, note):
        if self.checkNoteExists(note):
            self.notesList.remove(note)
        else: 
            print("Can not delete nonExistant Node")
        

    def searchByTitle(self, title):
        notes = filter(lambda note: note.title == title, board.notesList)
        self.notePrinter(notes)

        return list(notes)
    # needs to be modified to search by tags
    def searchByTag(self, tags):
        notes = filter(lambda note: note.tags == tags, board.notesList)
        self.notePrinter(notes)

        return list(notes)

    def searchByText(self, text):
        notes = filter(lambda note: note.text == text, board.notesList)
        self.notePrinter(notes)
        return notes

    def checkNoteExists(self, givenNote):
        for note in self.notesList:
            if note == givenNote:
                return True
        return False

    def notePrinter(self, notes):
        for note in notes:
            print(note.title)
            print(note.text)
            print(note.tags)


board = Board()
note1 = Note("Note1", "This is note 1 content", ["tag1.1", "tag1.2", "tag1.3"])
note2 = Note("Note2", "This is note 2 content", ["tag2.1", "tag2.2", "tag2.3"])
note3 = Note("Note3", "This is note 3 content", ["tag3.1", "tag3.2", "tag3.3"])

board.addNote(note1)
board.addNote(note2)
board.addNote(note3)

board.searchByTitle("Note1")
board.searchByText("This is note 2 content")
board.searchByTag(["tag3.1", "tag3.2", "tag3.3"])
