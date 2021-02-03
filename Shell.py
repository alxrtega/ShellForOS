#! /usr/bin/env python3
# alex ortega

import os, re, sys

class Shell:

    def __init__(self):
        self.prompt()

    def prompt(self):
        while 1:
            terminal = self.pathLine()
            os.write(1, (terminal + "\n").encode())
            if terminal == "exit":
                sys.exit(0)

    def pathLine(self):
        terminal = os.getcwd() + "\n$ "
        os.write(2, (terminal).encode())
        userInput = os.read(0, 128)
        userInput = userInput.decode().split("\n")
        userInput = userInput[0]
        userInput = str(userInput)
        return userInput

shell = Shell()