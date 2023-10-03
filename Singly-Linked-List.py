class Node:
    def __init__(self,value,next_Node = None):
        self.value = value
        self.nextNode = next_Node

class Linked_List:
    def __init__(self,head = None):
        self._head = head

    def append(self,value):
        node = Node(value)
        if self._head is None:
            self._head = node
            return
        currentNode = self._head
        while True:
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            else:
                currentNode = currentNode.nextNode

    def popped(self,value):
        currentNode = self._head
        prevNode = None
        target = False
        while currentNode and target is False:
            if currentNode.value == value:
                target = True  
            else:
                prevNode = currentNode  
                currentNode = currentNode.nextNode      
        if currentNode is None:
                print("Number isn't in the list!")
                return
        if prevNode is None:
            self._head = currentNode.nextNode
        else:
            prevNode.nextNode = currentNode.nextNode
            
    def Print(self):
        currentNode = self._head
        while True:
            if currentNode is None:
                print("None")
                break
            else:
                print(currentNode.value,"->", end=" ")
                currentNode = currentNode.nextNode

example = Linked_List()
example.append(1)
example.append(2)
example.append(3)
example.append(4)
example.append(5)
example.append(6)
example.append(7)
example.append(8)
example.Print()
example.popped(5)
example.Print()

