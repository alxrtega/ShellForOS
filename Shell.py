#! /usr/bin/env python3
# alex ortega

import os, re, sys

class Shell:

    def __init__(self):
        self.prompt()

    def prompt(self):

        while 1:
            userInput = self.pathLine()

            os.write(1, (userInput + "\n").encode())
            if userInput == "exit":
                sys.exit(0)

    def pathLine(self):
        message = os.getcwd() + "\n$ "
        os.write(2, (message).encode())
        userInput = os.read(0, 128)
        userInput = userInput.decode().split("\n")
        userInput = userInput[0]
        userInput = str(userInput)

        return userInput

shell = Shell()