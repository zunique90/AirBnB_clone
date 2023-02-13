#!/usr/bin/python3
# This is the entry point to the console made for the AirBnB clone

import cmd
import re
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

    def __init__(self, *args, **kwargs):
        self.__method_map = {
            'show': self.show_model,
            'all': self.print_all,
            'count': self.count_all,
            'destroy': self.destroy_model,
            'update': self.update_model
        }

        super().__init__(*args, **kwargs)

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

    def method_allowed(self, name):
        """
        Checks if a method is allowed
        Arguments:
            name: the name of the method
        Returns:
            True if method is allowed else False
        """
        return name in self.__method_map

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

        Usage: create <model>
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
        args_list = args.split()
        clean_list = []
        index = 0
        while index < len(args_list):
            if '"' in args_list[index] and '"' in args_list[index + 1]:
                # This means both strings are meant to be one word, not seperate words
                first_word = args_list[index].strip('"')
                second_word = args_list[index + 1].strip('"')
                clean_list.append("{} {}".format(first_word, second_word))
                index = index + 1
            else:
                clean_list.append(args_list[index])
            index = index + 1
        return clean_list

    def do_show(self, args):
        """
        Prints the string representation of an instance
        based on the class name and id

        Usage: show <classname> <id>
        """
        args_list = self.parse_args(args)
        self.show_model(args_list)
        
    def show_model(self, args_list):
        """
        Prints the string representation of an instance
        based on the class name and id
        Arguments:
            (list) args_list: A list containing the model_name and the id.
                              [model_name, id]
        """
        if not args_list:  # i.e. no extra argument was passed
            print("** class name missing **")
        elif len(args_list) != 2:
            # i.e. extra arguments were given but greater or less than 2(no id)
            print("** instance id missing **")
        elif not self.model_exists(args_list[0]):
            print("** class doesn't exist **")
        else:
            [model_name, model_id] = args_list[:2]
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
            model_name = args_list[0]
        self.print_all([model_name])

    def print_all(self, args_list):
        """
        Prints the string representation of all instances 
        of model based on model_name
        Arguments:
            (list) args_list: A list containing the model_name.
                              [model_name]
        """
        model_name = args_list[0]
        if not self.model_exists(model_name):
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
        self.update_model(args_list)

    def update_model(self, args_list):
        """
        Updates an instance based on the class name
        and id by adding or updating attribute
        Arguments:
            (list) args_list: A list containing the model_name, id, attribute and value.
                              [model_name, id, attr, value]
        """
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
        self.destroy_model(args_list)

    def destroy_model(self, args_list):
        """
        Removes an instance from storage based on the model name and id
        Arguments:
            (list) args_list: A list containing the model_name and the id.
                              [model_name, id]
        """
        if not args_list:  # No extra arguments were passed, i.e. no classname
            print("** class name missing **")
        elif not self.model_exists(args_list[0]):
            print("** class doesn't exist **")
        elif len(args_list) < 2:  # i.e. id wasn't provided
            print("** instance id missing **")
        else:

            [model_name, model_id] = args_list[:2]
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

    def default(self, args):
        """Runs when an unrecognised command is passed to console"""
        result = self.parse_unrecognised_command(args)
        if not result:
            super().default(args)
        elif self.method_allowed(result['method']):
            args_list = [result['model'], *result['args']]
            method = result['method']
            method_call = self.__method_map[method]
            method_call(args_list)
        else:
            super().default(args)

    def parse_unrecognised_command(self, line):
        """Parses an unrecognised command and returns all parameters"""
        result = {
            "model": None,
            "method": None,
            "args": []
        }

        # this regular expression seperates the string into three segments
        # (1).(2).(3)
        reg_exp = r"(\S+)\.([a-z]+)\((.*)\)"
        res = re.search(reg_exp, line)
        if res:
            reg_exp_2 = r'"?([a-zA-Z\s\d-]+)"?'
            result['model'] = res.groups()[0]
            result['method'] = res.groups()[1]

            # this regular expression seperates the arguments into seperate words
            res_1 = re.findall(reg_exp_2, res.groups()[2])
            if res_1:
                result['args'] = [x.rstrip().lstrip() for x in res_1 if x.strip()]

            print(result)
        return result

    def count_all(self, args_list):
        """
        Prints the number of instances of model in storage based on model_name
        Arguments:
            (list) args_list: A list containing the model_name. [model_name]
        """
        model_name = args_list[0]
        if not self.model_exists(model_name):
            print("** class doesn't exist **")
        else:
            count = storage.count_all(model_name)
            print(count)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
