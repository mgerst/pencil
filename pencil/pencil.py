class Pencil:
    def __init__(self, durability=50):
        self.paper = ""
        self.durability = durability

    def write(self, message):
        self.paper += message
        self.durability -= len(message)
