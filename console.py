#!/usr/bin/python3

""" This module contains one class """

import cmd
import sys
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.__init__ import storage


class HBNBCommand(cmd.Cmd):
    """console class implimentation"""

    prompt = "(hbnb)"
    classes = {"BaseModel": "BaseModel",
               "User": "User",
               "Place": "Place",
               "State": "State",
               "City": "City",
               "Amenity": "Amenity"
               "Review": "Review"
               }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        quit()

    def do_EOF(self, arg):
        """exit on EOF"""
        print()
        exit()

    def emptyline(self):
        """empty line does not execute anything"""
        pass

    def do_create(self, arg):
        """create an insstance of a class"""
        if not arg:
            print("** class name missing **")
        elif arg not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            print(eval(HBNBCommand.classes[arg])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance based
        on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            k = "{}.{}".format(args[0], args[1])
            objs = storage.all()
            try:
                print(objs[k])
            except KeyError:
                print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and
        id (save the change into the JSON file).
        """
        args = arg.split()
        objs = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objs.keys():
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argl[0], argl[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name
        """
        args = arg.split()
        if len(args) > 0 and args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            objs = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    objs.append(obj.__str__())
                elif len(args) == 0:
                    objs.append(obj.__str__())
            print(objs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        objs = storage.all()
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objs.keys():
            print("** no instance found **")
        elif len(args) == 2:
            print("** attribute name missing **")
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
        elif len(args) == 4:
            obj = objs["{}.{}".format(args[0], args[1])]
            obj.__dict__.update({args[2]: args[3]})
            obj.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
