
class MyOutOfSizeException(Exception):
    pass

class MyEmptyStackException(Exception):
    pass

class Node:
    def __init__(self, donnee):
        self.__donnee = donnee
        self.__next = None

    @property
    def donnee(self):
        return self.__donnee

    @property
    def next(self):
        return self.__next

    def set_next(self, next):
        self.__next = next


class Mystack:
    def __init__(self, size):
        self.__size = size
        self.__sommet = None

    def add_to_stack(self, element):
        if self.is_full():
            raise MyOutOfSizeException('La pile est pleine')
        new_node = Node(element)
        new_node.set_next(self.sommet)
        self.set_sommet(new_node)

    def is_empty(self):
        return self.sommet is None

    def is_full(self):
        return self.size == self.taille()

    def pop_from_stack(self):
        if self.is_empty():
            raise MyEmptyStackException('La pile est vide')
        donnee = self.sommet.donnee
        self.set_sommet(self.sommet.next)
        return donnee

    def sommet_element(self):
        return self.sommet.donnee if self.sommet else None

    def taille(self):
        count = 0
        current = self.sommet
        while current:
            count += 1
            current = current.next
        return count

    @property
    def size(self):
        return self.__size

    def set_size(self, size):
        self.__size = size

    @property
    def sommet(self):
        return self.__sommet

    def set_sommet(self, sommet):
        self.__sommet = sommet


myStack = Mystack(3)
myStack.add_to_stack('hello')
myStack.add_to_stack('hello')
print(myStack.is_full()) # False
myStack.add_to_stack('hello')
print(myStack.is_full()) # True
try:
    myStack.add_to_stack('hello')
except MyOutOfSizeException as e:
    print(e)
print(myStack.pop_from_stack()) # hello
print(myStack.is_empty()) # False
print(myStack.pop_from_stack()) # hello
print(myStack.is_empty()) # False
print(myStack.pop_from_stack()) # hello
print(myStack.is_empty()) # True
try:
    print(myStack.pop_from_stack())
except MyEmptyStackException as e:
    print(e)
