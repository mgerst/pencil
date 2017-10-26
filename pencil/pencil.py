class Pencil:
    """
    Represents a pencil that can write and erase messages.
    """
    DEFAULT_DURABILTY = 50
    ERASER_DURABILTY = 50

    def __init__(self, durability=DEFAULT_DURABILTY, length=10, eraser_durability=ERASER_DURABILTY):
        self.paper = ""
        self.durability = durability
        self.starting_durability = durability
        self.length = length
        self.eraser_durability = eraser_durability

    def write(self, message):
        """
        Write a message to the paper.

        Writing text will consume durability with the
        following rules:

        * spaces are free
        * uppercase costs 2
        * everything else costs 1

        :param message: The message to write
        """
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
        """
        Sharpen the pencil.

        If then pencil has run out of length, this will
        do nothing. Otherwise this will reset the
        durability and consume one unit of length.
        """
        if self.length == 0:
            return

        self.durability = self.starting_durability
        self.length -= 1

    def erase(self, text):
        """
        Erase the last occurrence of the given text.

        :param text: The text to erase
        """
        start_index = self.paper.rfind(text)
        end_index = start_index + len(text)

        for i in range(end_index, start_index, -1):
            if self.eraser_durability == 0:
                break

            cost = 1
            if text[-1] == " ":
                cost = 0
            text = text[:-1]

            # Calcuate the offset from the start
            i = i - start_index

            # Replace the character and update the durability
            self.paper = self.paper[0:start_index + i - 1] + " " + self.paper[start_index+i:]
            self.eraser_durability -= cost

    def edit(self, text, offset):
        """
        Edit text on the paper at a given offset.

        The written text will consume the pencil's durability the same
        as using :py:meth:`Pencil.write`.

        :param text: The text to write on the paper
        :param offset: The zero-indexed offset to start writing at
        """
        end_index = offset + len(text)

        replacement = ""
        cost = 0
        for i in range(len(text)):
            start_index = offset + i

            if self.paper[start_index] == " ":
                if self.durability - cost == 0:
                    replacement += " "
                    continue

                replacement_char = text[i]
                if text[i] != " ":
                    cost += 1
                elif text[i].isupper():
                    cost += 2
            else:
                if self.durability - cost == 0:
                    continue

                replacement_char = "@"
                cost += 1

            replacement += replacement_char

        self.paper = self.paper[0:offset] + replacement + self.paper[end_index:]
        self.durability -= cost

