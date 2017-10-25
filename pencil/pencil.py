class Pencil:
    DEFAULT_DURABILTY = 50
    ERASER_DURABILTY = 50

    def __init__(self, durability=DEFAULT_DURABILTY, length=10, eraser_durability=ERASER_DURABILTY):
        self.paper = ""
        self.durability = durability
        self.starting_durability = durability
        self.length = length
        self.eraser_durability = eraser_durability

    def write(self, message):
        for char in message:
            cost = 1
            if self.durability == 0:
                cost = 0
                char = " "
            elif char.isupper():
                cost = 2
            elif char == " " or char == "\n":
                cost = 0

            self.paper += char
            self.durability -= cost

    def sharpen(self):
        if self.length == 0:
            return

        self.durability = self.starting_durability
        self.length -= 1

    def erase(self, text):
        start_index = self.paper.rfind(text)
        end_index = start_index + len(text)
        replacement = " " * len(text)

        self.paper = self.paper[0:start_index] + replacement + self.paper[end_index:]
        self.eraser_durability -= len(text)
