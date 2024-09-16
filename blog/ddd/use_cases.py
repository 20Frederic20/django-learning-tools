

class UseCases():
    def __init__(self, storage):
        self.storage = storage
    def create_note(self, title, body):
        note = Note(title, body)
        return self.storage.save_note(note)