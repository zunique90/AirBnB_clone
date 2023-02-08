#!/usr/bin/python3
# This is the entry point to the console made for the AirBnB clone

import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class controls the features of the AirBnB console"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quits the terminal"""
        # self.close()
        return True

    def help_quit(self):
        """Prints the helper test for the quit command"""
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Quits the terminal"""
        # self.close()
        return True

    def help_EOF(self):
        """Prints the helper test for the EOF command"""
        print("Quit command to exit the program")

    def do_create(self, args):
        """Creates a new instance of BaseModel
        saves it (to the JSON file) and prints the id"""
        if not args:
            print("** class name missing **")
        elif args != 'BaseModel':
            print(BaseModel.__class__.__name__)
            print("** class doesn't exist **")
        else:
            model = BaseModel()
            model.save()
            print(model.id)

    def help_create(self):
        """Prints the helper test for the create command"""
        print("Creates a new instance of BaseModel, saves it",
        "(to the JSON file) and prints the id")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
