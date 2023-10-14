#!/usr/bin/python3
"""
This module defines the entry point of the command interpreter.
"""

import cmd


class HBNBCommand(cmd.Cmd):
    """
    This class defines the command interpreter.
    """
    prompt = "(hbnb)"

    def do_quit(self, arg):
        """
        Quit command to exit the program.
        """
        return True

    def do_EOF(self, arg):
        """
        EOF command to exit the program.
        """
        print()
        return True

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything.
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
