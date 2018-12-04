"""
Names: Zack Dowling & Matthew Norloff
File: phonebookserver.py
Module 6 Phonebook Assignment
Server for providing phonebook access.
Uses client handlers to handle clients' requests.
Creates a single phonebook for all clients.
"""

from phonebook import Phonebook
from socket import *
from phonebookclienthandler import PhonebookClientHandler
import threading

# In this example, it is set to local host
HOST = ''
PORT = 8888
ADDRESS = (HOST, PORT)

phonebook = Phonebook() # called from the phonebook.py
ThreadedServer = socket(AF_INET, SOCK_STREAM)
ThreadedServer.bind(ADDRESS)
ThreadedServer.listen(5)

while True:
    print("Waiting for connection . . .")
    client, address = ThreadedServer.accept()
    print("... connected from: ", address)
    # send the starting book to the
    # client.send(bytes(start_book.encode()))
    # The handlers share the phonebook
    # Multiple clients can connect to the phonebook
    handler = PhonebookClientHandler(client, phonebook)
    handler.start()
