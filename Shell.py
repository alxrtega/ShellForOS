#! /usr/bin/env python3
# alex ortega

import os, re, sys

class Shell:

    # File Descriptors:
    #       0: input
    #       1: output

    def __init__(self):
        self.prompt()

    def prompt(self):
        while 1:
            command = self.getCommand()
            if command == "exit":
                sys.exit(0)
            elif command == "":
                pass
            elif command[0] == "#":
                pass
            elif command[0:2] == "cd":
                command = command.split()
                self.changeDirectory(command[1])
            elif ">" in command or "<" in command:
                self.redirection(command)
            else:
                self.execute(command)

    def getCommand(self):
        os.write(1, (os.getcwd() + "\n$ ").encode())
        userInput = os.read(0, 128)
        userInput = userInput.strip()
        userInput = userInput.decode().split("\n")
        userInput = userInput[0]
        userInput = str(userInput)
        return userInput

    def changeDirectory(self, path):
        try:
            os.chdir(path)
        except:
            os.write(1, "No such directory\n".encode())

    def execute(self, command):
        pid = os.fork() 
        if pid == 0: 
            self.runEXECVE(command)
        elif pid > 0: 
            os.wait() 
        else:
            print("fork() failed")

    def runEXECVE(self, command):
        line = command.split()
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir, line[0])
            try:
                os.execve(program, line, os.environ) 
            except:                
                pass
        os.write(1, ("shell: "+ line[0] +" command not found\n").encode())
        sys.exit(0)

    def redirection(self, command):
        pid = os.fork() 
        if pid == 0:
            if ">" in command:
                command = command.split(">")
                os.close(1)
                os.open(command[1], os.O_CREAT | os.O_WRONLY)
                os.set_inheritable(1,True)

            else:
                command = command.split("<")
                os.close(0)
                os.open(command[1], os.O_RDONLY)
                os.set_inheritable(0, True)

            self.runEXECVE(command[0])
        elif pid > 0:
            os.wait()
        else:
            print("redirection() failed")

shell = Shell()