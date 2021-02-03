#! /usr/bin/env python3
# alex ortega

import os, re, sys

class Shell:

    def __init__(self):
        self.prompt()

    def prompt(self):
        while 1:
            terminal = self.pathLine()
            if terminal == "exit":
                sys.exit(0)
            else:
                self.execute(terminal)

    def pathLine(self):
        terminal = os.getcwd() + "\n$ "
        os.write(2, (terminal).encode())
        userInput = os.read(0, 128)
        userInput = userInput.decode().split("\n")
        userInput = userInput[0]
        userInput = str(userInput)
        return userInput

    def execute(self, command):
        pid = os.fork() 
        if pid == 0: 
            line = command.split()
            for dir in re.split(":", os.environ['PATH']):
                program = "%s/%s" % (dir, line[0])
                try:
                    os.execve(program, line, os.environ) 
                except:                
                    pass
            print("Shell: "+ line[0] +" command not found")
            sys.exit(0)
        elif pid > 0 : 
            os.wait() 
        else:
            print("fork() failed")

shell = Shell()