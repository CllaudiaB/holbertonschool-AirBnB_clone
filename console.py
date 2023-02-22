#!/usr/bin/python3
"""Created class"""
import cmd
import sys
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class HBNBCommand(cmd.Cmd):
    """Created a class that contains the entry point of the command interpreter
    """
    prompt = '(hbnb)'
    class_name = ["BaseModel"]

    def do_EOF(self, arg):
        """EOF command to exit the program
        """
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def emptyline(self):
        """Passed an empty line when ENTER
        """
        pass

    def do_create(self, arg):
        """create a new instance of BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in self.class_name:
            print("** class doesn't exist **")
        else:
            instance = eval(arg)()
            instance.save()
            print(instance.id)

    """def do_destroy(self, arg):
        Deletes an instance based on the class name and id
        
        arg = line.split(" ")
        if arg == 0:
            print("** class name missing **")
        elif arg[1] is not class_name:
            print("** class doesn't exist **")
        elif arg < 2:
            print("** instance id missing **")
        elif 
            print("** no instance found **")
        else:
            del"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()
