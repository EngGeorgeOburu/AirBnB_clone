#!/usr/bin/python3
""" Class for the cmd module """
import cmd
import models

class HBNBCommand(cmd.Cmd):
    """Command interpretor class."""
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """ Quit command to exit the program """
        return True

    def help_quit(self):
        """ Help message for the quitting the programm """
        print("Quit command to exit the program")

    def do_EOF(self, arg):
        """Exit the prpgram when end of line is reached using 'CTRL + C'"""
        print("")
        return True

    def d0_empty(self):
        """ Do nothing if the empty command is passed."""
        pass
    def do_create(self, arg):
        """Create a new instance of BaseModel and then saves it."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** Class doesn't exist **")
            return 

        new_instance = models.classes[args[0]]()
        new_instance.save ()
        print(new_instance.id)

    def do_show(self, arg):
        """ Printing string representation of an instance."""
        args = arg.split()
        if not args:
            print("** Class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id is missing **")
            return

        key = args[0] + ',' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        print(models.storage.all()[key])

    def do_destroy(self, arg):
        """ Deletes an instance based on the class name and id."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return

        key = args[0] + ',' + args[1]
        if key not in models.storage.all():
            print("** noinstance found **")
            return
        del models.storge.all()[key]
        models.storage.save()

    def do_all(self, arg):
        """Printing string representation of all instances."""
        if arg and arg not in models.classes:
            print("** class doesn't exist **")
            return
        instance_list = []
        for key, obj in models.storage.all().items():
            if arg:
                if type(obj).__name__ == arg:
                    instance_list.append(str(obj))
            else:
                instance_list.append(str(obj))
                print(instance_list)

    def do_update(self, arg):
        """ Updates an instance by adding or updating attribute."""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in models.classes:
             print("** class doesn't exist **")
             return
        if len(args) < 2:
            print("** instance id is missing **")
            return

        key = args[0] + ',' + args[1]
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        setattr(models.storage.all()[key], args[2], args[3])
        models.storage.all()[key].save()

if __name__ == "__main__":
    HBNBCommand().cmdloop()
