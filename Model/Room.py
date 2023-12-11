class Room:

    def __init__(self):
        self.id = None
        self.messages = []

    def set_id(self, id):
        self.id = id

    def add_message(self, message):
        self.messages.append(message)