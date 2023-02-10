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
              "Also, prints the id.\n\t", "Usage: create BaseModel\n", sep='\n')

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
            model_data = storage.get_object(model_id, model_name)
            if model_data:
                model = BaseModel(**model_data)
                print(model)
            else:
                print("** no instance found **")

    def help_show(self):
        """Prints the helper text for the show command"""

        print("Prints the string representation of an instance based on the \
        class name and id\n\t", "Usage: show <classname> <id>\n", sep='\n')

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
            model_list = [str(BaseModel(**model)) for model in storage.all().values()]
            print(model_list)

    def help_all(self):
        """Prints the help text for the all command"""

        print("Prints all string representation of all instances based on the \
        classname passed as an argument.\n\t", "Usage: all <classname>",
              "Classname is optional, default is BaseModel\n", sep='\n')

    def do_update(self, args):
        """
        Updates an instance based on the class name and id by adding or updating attribute

        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args_list = self.parse_args(args)

        if not args_list: # No extra arguments were passed, i.e. no classname
            print("** class name missing **")
        elif args_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args_list) < 2: # i.e. id wasn't provided
            print("** instance id missing **")
        elif len(args_list) < 3: # i.e. attribute name wasn't provided
            print("** attribute name missing **")
        elif len(args_list) < 4: # i.e. value wasn't provided
            print("** value missing **")
        else:

            IGNORE = ['id', 'created_at', 'updated_at']

            [model_name, model_id, attr_name, value] = args_list[:4]

            model_data = storage.get_object(model_id, model_name)
            if model_data:
                if attr_name not in IGNORE:
                    model = BaseModel(**model_data)
                    setattr(model, attr_name, value)
                    model.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """Prints the help text for the update command"""

        print('Updates an instance based on the class name and id by adding or \
        updating attribute\n\t', 'Usage: update <class name> <id> \
        <attribute name> "<attribute value>"\n', sep='\n')

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """

        args_list = self.parse_args(args)

        if not args_list: # No extra arguments were passed, i.e. no classname
            print("** class name missing **")
        elif args_list[0] != 'BaseModel':
            print("** class doesn't exist **")
        elif len(args_list) < 2: # i.e. id wasn't provided
            print("** instance id missing **")
        else:

            [model_name, model_id] = args_list
            key = storage.generate_key(model_id, model_name)
            status = storage.destroy_object(key)
            if not status: # i.e. unable to delete object
                print("** no instance found **")

    def help_destroy(self):
        """Prints the help text for the destroy command"""

        print("""
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """)
if __name__ == '__main__':
    HBNBCommand().cmdloop()
