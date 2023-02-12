#!/usr/bin/python3
# This is the entry point to the console made for the AirBnB clone

import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """This class controls the features of the AirBnB console"""

    prompt = '(hbnb) '
    __default_model = 'BaseModel'
    __models = {
        'BaseModel': BaseModel,
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def use_model(self, _name, *args, **kwargs):
        """
        Gets the right model to be used based on _name
        Arguments:
            (string) _name: the name of the model we need to use
        Returns:
            An instance of the model
        """
        return self.__models[_name](*args, **kwargs)

    def model_exists(self, name):
        """
        Checks if a model exists
        Arguments:
            name: the name of the model
        Returns:
            True if model exists else False
        """
        return name in self.__models

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
        elif not self.model_exists(args):
            print("** class doesn't exist **")
        else:
            model = self.use_model(args)
            model.save()
            print(model.id)

    def help_create(self):
        """Prints the helper text for the create command"""

        print(
            "Creates a new instance of BaseModel saves it (to the JSON file).",
            "Also, prints the id.\n\t", "Usage: create BaseModel\n", sep='\n'
            )

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
        if not args_list:  # i.e. no extra argument was passed
            print("** class name missing **")
        elif len(args_list) != 2:
            # i.e. extra arguments were given but greater or less than 2(no id)
            print("** instance id missing **")
        elif not self.model_exists(args_list[0]):
            print("** class doesn't exist **")
        else:
            [model_name, model_id] = args_list
            model_data = storage.get_object(model_id, model_name)
            if model_data:
                model = self.use_model(model_name, **model_data)
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

        model_name = self.__default_model
        if args and isinstance(args_list, list):
            print('is list')
            model_name = args_list[0]

        if args and not self.model_exists(model_name):
            print("** class doesn't exist **")
        else:
            model_list = [
                    str(self.use_model(model_name, **model_data))
                    for model_data in storage.get_all(model_name).values()
                    ]
            print(model_list)

    def help_all(self):
        """Prints the help text for the all command"""

        print("Prints all string representation of all instances based on the \
        classname passed as an argument.\n\t", "Usage: all <classname>",
              "Classname is optional, default is BaseModel\n", sep='\n')

    def do_update(self, args):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """

        args_list = self.parse_args(args)

        if not args_list:  # No extra arguments were passed, i.e. no classname
            print("** class name missing **")
        elif not self.model_exists(args_list[0]):
            print("** class doesn't exist **")
        elif len(args_list) < 2:  # i.e. id wasn't provided
            print("** instance id missing **")
        elif len(args_list) < 3:  # i.e. attribute name wasn't provided
            print("** attribute name missing **")
        elif len(args_list) < 4:  # i.e. value wasn't provided
            print("** value missing **")
        else:

            IGNORE = ['id', 'created_at', 'updated_at']

            [model_name, model_id, attr_name, value] = args_list[:4]

            key = storage.generate_key(model_id, model_name)
            model_data = storage.get_object(key=key)
            if model_data:
                if attr_name not in IGNORE:
                    model = self.use_model(model_name, **model_data)
                    setattr(model, attr_name, value)
                    model.save()
            else:
                print("** no instance found **")

    def help_update(self):
        """Prints the help text for the update command"""

        print('Updates an instance based on the class name and id by adding or\
        updating attribute\n\t', 'Usage: update <class name> <id>\
        <attribute name> "<attribute value>"\n', sep='\n')

    def do_destroy(self, args):
        """
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """

        args_list = self.parse_args(args)

        if not args_list:  # No extra arguments were passed, i.e. no classname
            print("** class name missing **")
        elif not self.model_exists(args_list[0]):
            print("** class doesn't exist **")
        elif len(args_list) < 2:  # i.e. id wasn't provided
            print("** instance id missing **")
        else:

            [model_name, model_id] = args_list
            key = storage.generate_key(model_id, model_name)
            status = storage.destroy_object(key)
            if not status:  # i.e. unable to delete object
                print("** no instance found **")

    def help_destroy(self):
        """Prints the help text for the destroy command"""

        print("""
        Deletes an instance based on the class name and id

        Usage: destroy <class name> <id>
        """)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
