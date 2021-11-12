#!/usr/bin/env python3

""" This module contains one class """

import cmd
import sys


class HBNBCommand(cmd.Cmd):
    """console class implimentation"""

    prompt = "(hbnb)"

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


if __name__ == "__main__":
    HBNBCommand().cmdloop()
