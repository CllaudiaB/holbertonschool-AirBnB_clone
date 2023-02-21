#!/usr/bin/python3
import cmd

"""Created class"""

class HBNBCommand(cmd.Cmd):
    """
    Created a class that contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, line):
        """Quit command to exit the program
        """

        return True

    def emptyline(self):
        """
        Passed an empty line when ENTER
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()
