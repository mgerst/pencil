class Pencil:
    def __init__(self, durability=50):
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
