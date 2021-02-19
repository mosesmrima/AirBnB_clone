#!/usr/bin/python3
import cmd
""" module contains the console implementation"""


class HBNBCommand(cmd.Cmd):
    """console for HBnB"""
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """exit console"""
        print("")
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
