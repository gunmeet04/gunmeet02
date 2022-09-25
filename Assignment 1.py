class Node:
    def _init_(self, s, x):
        self.age = 0
        self.name = ""
        self.next = None
        self.prev = None

        self.name = s
        self.age = x
        self.prev = None
        self.next = None

def main():
    father = Node("Kanwaljit Singh", 47)
    mother = Node("Harvinder Kaur", 42)
    brother = Node("Jaskaran Singh", 18)
    sister = Node("Arnoor Kaur", 14)
    myself = Node("Gunmeet Singh", 19)

    head = father

    father.prev = None
    father.next = mother
    mother.prev = father
    mother.next = brother
    brother.prev = mother
    brother.next = sister
    sister.prev = mother
    sister.next = myself
    myself.prev = sister
    myself.next = None

    Globals.printdll(head)


class Globals:

    def printdll(head):
        while head is not None:
            print(head.name, end = '')
            print("-", end = '')
            print(head.age, end = '')
            print("     ", end = '')
            head = head.next

if _name_ == "_main_":
    main()
