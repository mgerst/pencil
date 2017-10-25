class Pencil:
    DEFAULT_DURABILTY = 50

    def __init__(self, durability=DEFAULT_DURABILTY, length=10):
        self.paper = ""
        self.durability = durability
        self.starting_durability = durability
        self.length = length

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
        self.durability = self.starting_durability
        self.length -= 1
