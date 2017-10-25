class Pencil:
    DEFAULT_DURABILTY = 50

    def __init__(self, durability=DEFAULT_DURABILTY):
        self.paper = ""
        self.durability = durability

    def write(self, message):
        for char in message:
            cost = 1
            if char.isupper():
                cost = 2
            elif char == " " or char == "\n":
                cost = 0

            self.paper += char
            self.durability -= cost
