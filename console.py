#!/usr/bin/python3
# This is the entry point to the console made for the AirBnB clone

import cmd


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

if __name__ == '__main__':
    HBNBCommand().cmdloop()
