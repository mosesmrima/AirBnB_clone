#!/usr/bin/python3
"""This module contains the parser module"""
import re
from shlex import split


def parse(arg):
    """
    This function parses the cmd arguments passed by the user to the console
    :param arg: a string of passed arguments
    :return: returns a list of arguments
    """
    brackets = re.search(r"\[(.*?)\]", arg)
    braces = re.search(r"\{(.*?)\}", arg)
    if braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            tokens = split(arg[:brackets.span()[0]])
            arg_l = [i.strip(",") for i in tokens]
            arg_l.append(brackets.group())
            return arg_l
    else:
        tokens = split(arg[:braces.span()[0]])
        arg_l = [i.strip(",") for i in tokens]
        arg_l.append(braces.group())
        return arg_l
