"""An example of how to use inheritance in Python using SuperClasses
and SubClasses.

Author: Trey Hamilton
Date: 5/4/2018
"""


class SuperClass:

    def __init(self, Id, name):
        self.name = name
        self.Id = Id

    def print_name(self):
        print("Your name is {}".format(self.name))

    def add_id_to_array(self):
        new_array = []
        new_array.append(self.Id)
        print(new_array)


class SubClass(SuperClass):

    def __init__(self, Id, name):
        self.Id = Id
        self.name = name
        SuperClass.__init__(self)


sub = SubClass(1, 'Trey')
sub.add_id_to_array()
sub.print_name()
