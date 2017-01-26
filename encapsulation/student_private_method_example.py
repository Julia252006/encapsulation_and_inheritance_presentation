class Student:
    def __init__(self, name):
        self.__name = name

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def __step(self):
        print("%s make step." % self.__name)

    def going_home(self):
        self.__step()

    name = property(get_name, set_name)


student = Student('Bob')

try:
    print(student.__name)  # accessing a private attribute
except AttributeError:
    print("\t{}: name {}".format(AttributeError.__name__, AttributeError.__doc__))

try:
    print(student.__step())  # accessing a private attribute
except AttributeError:
    print("\t{}: step() {}".format(AttributeError.__name__, AttributeError.__doc__))


# public method invocation --> all is OK
student.going_home()
# public method invocation --> all is OK
student.set_name("Alice")
student.going_home()

# accessing an attribute via its property object
student.name = 'Mark'
print(student.name)