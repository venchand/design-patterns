'''

The singleton pattern is a design pattern that restricts the instantiation of a class to one object.
'''

## BORG pattern - used for singleton
# Singleton Borg pattern
class Borg:

    # state shared by each instance
    __shared_state = dict()

    # constructor method
    def __init__(self):

        self.__dict__ = self.__shared_state
        self.state = 'GeeksforGeeks'

    def __str__(self):

        return self.state


# main method
if __name__ == "__main__":

    person1 = Borg()    # object of class Borg
    person2 = Borg()    # object of class Borg
    person3 = Borg()    # object of class Borg

    person1.state = 'DataStructures'  # person1 changed the state
    person2.state = 'Algorithms'     # person2 changed the state

    print(person1)    # output --> Algorithms
    print(person2)    # output --> Algorithms

    person3.state = 'Geeks'  # person3 changed the
    # the shared state

    print(person1)    # output --> Geeks
    print(person2)    # output --> Geeks
    print(person3)    # output --> Geeks




## AFTER Singleton

# classic implementation of Singleton Design pattern
class Singleton:

    __shared_instance = 'GeeksforGeeks'

    @staticmethod
    def getInstance():
        """Static Access Method"""
        if Singleton.__shared_instance == 'GeeksforGeeks':
            Singleton()
        return Singleton.__shared_instance

    def __init__(self):
        """virtual private constructor"""
        if Singleton.__shared_instance != 'GeeksforGeeks':
            raise Exception("This class is a singleton class !")
        else:
            Singleton.__shared_instance = self


# main method
if __name__ == "__main__":

    # create object of Singleton Class
    obj = Singleton()
    print(obj)

    # pick the instance of the class
    obj = Singleton.getInstance()
    print(obj)
