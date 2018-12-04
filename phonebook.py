"""
Names: Zack Dowling & Matthew Norloff
File: phonebook.py
Module 6 Phonebook Assignment
This MODULE includes the main function which tests the phone book data structure.
"""


class Phonebook(object):
    """Represents a phone book."""

    def __init__(self):
        self.entries = {}

    def add(self, name, number):
        """Adds the name and number to the phone book."""
        self.entries[name] = number

    def get(self, name):
        """Returns the number if name is in the phone book,
        or None otherwise."""
        return self.entries.get(name, None)

    def __str__(self):
        """Returns the string representation of the phone book."""
        result = ""
        keys = list(self.entries.keys()) # read the phonebook into a list
        keys.sort() # sort the list
        for key in keys:
            result += key + ":" + self.entries[key] + "\n"
        return result


def main():
    """
        Testing function for PhoneBook.
        The main function is not meant to be called directly from the other programs
    """
    book = Phonebook() # instantiate the phonebook class into a phonebook object
    for name in range(10):
        # This loop is for testing purpose
        # in actual phone book app, this main is not called
        #
        book.add("Name" + str(name), "524-4682")
    print(book)
    for name in range(10):
        print(book.get("Name" + str(name)))

if __name__ == "__main__":
    main()