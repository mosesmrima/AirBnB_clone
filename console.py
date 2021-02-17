#!/usr/bin/python3
""" module contains the console implementation"""
import cmd
from models.base_model import BaseModel
from models import storage


def parse(arg):
    """parses commandline arguments"""
    args = arg.split(" ")
    return args


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit console"""
        print("")
        return True

    def emptyline(self) -> bool:
        pass

    def do_create(self, arg):
        """creates a new class instance"""
        args = parse
        if len(arg) == 0:
            print("** class name missing **")
        elif arg not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj = BaseModel()
            print(obj.id)
            storage.save()

    def do_show(self, arg):
        """prints all the instances"""
        args = parse(arg)
        objdict = storage.all()
        if len(args) == 0:
            print(args)
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(args[0], args[1])])


if __name__ == '__main__':
    HBNBCommand().cmdloop()
