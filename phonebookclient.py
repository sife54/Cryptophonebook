"""
File: phonebookclient.py
Project: Phonebook client server program
Client for a phone book application.
Sends the commands ADD <name> <number> or FIND <name> to the server.
update
"""

import socket
from codecs import decode
from breezypythongui import EasyFrame
from Crypto.Cipher import AES
from decrypto import decrypt
import re
import os

hostname = socket.gethostname()
HOST = socket.gethostbyname(hostname)
PORT = 8888
BUFSIZE = 1024
ADDRESS = (HOST, PORT)
CODE = "utf-8"

key = b'\xbf\xc0\x85)\x10nc\x94\x02)j\xdf\xcb\xc4\x94\x9d(\x9e[EX\xc8\xd5\xbfI{\xa2$\x05(\xd5\x18'
cipher = AES.new(key)


def pad(s):
    return s + ((16-len(s) % 16) * "{")


def encrypt(plaintext):                     # uses pad and the cipher key to encrypt
    global cipher
    return cipher.encrypt(pad(plaintext))


class PhonebookClient(EasyFrame):
    """GUI for the client app."""

    def __init__(self):
        """Initialize the frame and widgets."""
        EasyFrame.__init__(self, title="Phone Book")
        # Add the labels, fields, and button
        self.statusLabel = self.addLabel(text="Do you want to connect to the Phonebook?",
                                         row=0,
                                         column=0,
                                         columnspan=3)

        self.find = self.addButton(row=1,
                                      column=0,
                                      text="Find",
                                      command=self.find,
                                      state="disabled")

        self.addTo = self.addButton(row=1,
                                     column=1,
                                     text="Add",
                                     command=self.add,
                                     state="disabled")

        self.connect = self.addButton(row=1,
                                      column=2,
                                      text="Connect",
                                      command=self.connect)

        self.update = self.addButton(row=11,
                                     column=2,
                                     text="Update",
                                     command=self.update)

        self.Results = self.addTextArea("",row=2,
                                        column=0,
                                        rowspan=8,
                                        columnspan=4)

    def find(self):
        """Looks up a name in the phone book."""
        name = self.prompterBox(promptString="Enter the name.")
        if name == "": return
        self.server.send(bytes("FIND " + name, CODE))
        reply = decode(self.server.recv(BUFSIZE), CODE)
        if not reply:
            self.messageBox(message="Server disconnected")
            self.disconnect()
        else:
            self.statusLabel["text"] = reply

    def add(self):
        """Adds a name and number to the phone book."""
        name = self.prompterBox(promptString="Enter first initial followed by last name (EX: ZDowling).")
        if name == "": return
        number = self.prompterBox(promptString="Enter the phone number.")
        if number == "": return
        encrypt(name)
        encrypt(number)
        self.server.send(bytes("ADD " + name + " " + number, CODE))
        reply = decode(self.server.recv(BUFSIZE), CODE)
        if not reply:
            self.messageBox(message="Server disconnected")
            self.disconnect()
        else:
            self.statusLabel["text"] = reply

    def update(self):
        start_book = decrypt(self.server.recv(BUFSIZE)).decode()  # decrypts the update for input to results txt field

        self.Results.setText(start_book)

    def connect(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.connect(ADDRESS)
        start_book = decrypt(self.server.recv(BUFSIZE)).decode()   # decrypts and decodes the date from client handler

        self.Results.setText(start_book)
        self.statusLabel["text"] = decode(self.server.recv(BUFSIZE), CODE)
        self.connect["text"] = "Disconnect"
        self.connect["command"] = self.disconnect
        self.find["state"] = "normal"
        self.addTo["state"] = "normal"

    def disconnect(self):
        self.server.close()
        self.statusLabel["text"] = "Want to connect?"
        self.connect["text"] = "Connect"
        self.connect["command"] = self.connect
        self.find["state"] = "disabled"
        self.addTo["state"] = "disabled"


def main():
    """Instantiate and pop up the window."""
    PhonebookClient().mainloop()


if __name__ == "__main__":
    main()