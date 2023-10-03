class Node: #Creates a Node instance that contains the nodes value and pointer to the next node
    def __init__(self,value,next_Node = None):
        self.value = value # The Nodes value
        self.nextNode = next_Node # Pointer for the Next Node in the list

class Linked_List: # This class allows for Singly-Linked-List to be created and linked together
    def __init__(self,head = None):
        self._head = head # This is the head or start of the list
    
    # This is to add a Node to the tail of the Linked List
    def append(self,value):
        node = Node(value) # Creating a new Node with a value
        if self._head is None:	# This is incase the Linked List is empty
            self._head = node
            return
        currentNode = self._head
        while True: # This is for iterating through the linked list to find the tail and add the new Node
            if currentNode.nextNode is None:
                currentNode.nextNode = node
                break
            else:
                currentNode = currentNode.nextNode
    
    # Much like append() this is to "insert" a Node a specific position in the linked list
    # by tracking the current Nodes next point and the previous Nodes next pointer
    def Insert(self,value,where):
        currentNode = self._head
        target = False
        prevNode = None 
        while currentNode and target is False:
            if currentNode.value == where:
                target = True  
            else:
                prevNode = currentNode  
                currentNode = currentNode.nextNode
        if currentNode is None:
                print("That number doesn't exist!")	#Incase the node position isn't in the list
                return
        elif prevNode is None:
            node = Node(value)
            node.nextNode = currentNode	# This allows for a new Node to be added to the front of the list
            self._head = node
            return 
        else:
            node = Node(value)
            prevNode.nextNode = node
            node.nextNode = currentNode	# This puts the new Node in the selected spot of the list
            return 

    # This allows a Node to be removed from the list by keeping track of the current head and the previous head
    def popped(self,value): 
        currentNode = self._head
        prevNode = None
        target = False
        while currentNode and target is False: # This is iterate through the list for find the node to delete
            if currentNode.value == value:
                target = True  
            else:
                prevNode = currentNode  
                currentNode = currentNode.nextNode      
        if currentNode is None:
                print("Number isn't in the list!") # This is incase the node doesn't exist
                return
        if prevNode is None:
            self._head = currentNode.nextNode # This is for the number at the front of the list
        else:
            prevNode.nextNode = currentNode.nextNode
    
    # This method allows for the list to be printed out        
    def Print(self):
        currentNode = self._head
        while True:
            if currentNode is None:
                print("None")
                break
            else:
                print(currentNode.value,"->", end=" ") # uses "->" to point to the next node in the list
                currentNode = currentNode.nextNode

# Using the Class

example = Linked_List()
example.append(1)
example.append(2)
example.append(3)
example.append(4)
example.append(5)
example.append(6)
example.append(7)
example.append(8)
example.append(9)
example.append(10)
example.Print()
example.popped(5)
example.Print()
example.Insert(5,6)
example.Print()
example.popped(2)
example.Print()
example.Insert(2,3)
example.Print()
example.Insert(0,1)
example.Print()
example.Insert(-1,0)
example.Print()
