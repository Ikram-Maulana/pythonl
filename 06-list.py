class SinglyLinkedList:
    class _Node:
        def __init__(self, element, nextNode=None):
            self.element = element
            self.nextNode = nextNode

    def __init__(self):
        self._head = None
        self._size = 0

    # Untuk Output
    def __str__(self):
        result = ""
        pointer = self._head
        while pointer != None:
            result = result + str(pointer.element) + " "
            pointer = pointer.nextNode
        return result

    # Menambahkan Node di paling awal
    def add_first(self, element):
        newNode = self._Node(element)
        newNode.nextNode = self._head
        self._head = newNode
        self._size += 1

    # Untuk menghitung panjang
    def __len__(self):
        return self._size


def main():
    myList = SinglyLinkedList()
    myList.add_first(2020)
    myList.add_first(10)
    myList.add_first(27)
    print(str(myList))
    print("Panjang Node: %d" % (len(myList)))


main()
