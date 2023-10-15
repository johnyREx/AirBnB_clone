#!/usr/bin/env python3
"""Console module"""
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ quit command"""
        return True

    def do_EOF(self, arg):
        """Exit the program at end of file"""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
