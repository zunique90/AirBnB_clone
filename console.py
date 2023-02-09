#!/usr/bin/python3
# This is the entry point to the console made for the AirBnB clone

import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """This class controls the features of the AirBnB console"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """
        Quits the terminal

        Usage: quit
        """
        # self.close()
        return True

    def help_quit(self):
        """Prints the helper text for the quit command"""
        print("Quit command to exit the program\n")

    def do_EOF(self, arg):
        """
        Quits the terminal

        Usage: EOF
        """
        # self.close()
        return True

    def help_EOF(self):
        """Prints the helper text for the EOF command"""
        print("Quit command to exit the program\n")

    def do_create(self, args):
        """
        Creates a new instance of BaseModel saves it (to the JSON file)
        Also, prints the id

        Usage: create BaseModel
        """
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
        """Prints the helper text for the create command"""

        print("Creates a new instance of BaseModel saves it (to the JSON file).",
              "Also, prints the id.\n", "Usage: create BaseModel\n", sep='\n')

    def parse_args(self, args):
        """
        Parses the argument passed with command,
        returns a list of the arguments
        """
        return args.split()

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id

        Usage: show <classname> <id>
        """
        args_list = self.parse_args(args)
        if not args_list: # i.e. no extra argument was passed
            print("** class name missing **")
        elif len(args_list) != 2:
            # i.e. extra arguments were given but not up to or less than 2 (no id)
            print("** instance id missing **")
        elif args_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            [model_name, model_id] = args_list
            models = storage.all()
            key = "{}.{}".format(model_name, model_id)
            if key in models:
                model = BaseModel(models[key])
                print(model)
            else:
                print("** no instance found **")

    def help_show(self):
        """Prints the helper text for the show command"""

        print("Prints the string representation of an instance based on the \
        class name and id\n", "Usage: show <classname> <id>\n", sep='\n')

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based on the classname passed as an argument.

        Usage: all <classname>
        Classname is optional, default is BaseModel
        """

        args_list = self.parse_args(args)

        if args and args_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        else:
            model_dict = storage.all()
            model_list = []
            for model_key, model_data in model_dict.items():
                model = BaseModel(**model_data)
                model_list.append(str(model))

            print(model_list)

    def help_all(self):
        """Prints the help text for the all command"""

        print("Prints all string representation of all instances based on the \
        classname passed as an argument.\n", "Usage: all <classname>",
              "Classname is optional, default is BaseModel\n", sep='\n')

if __name__ == '__main__':
    HBNBCommand().cmdloop()
