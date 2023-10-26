from Linked_List import Linked_List

# Create the linked list
example = Linked_List()

# Adding elements to the linked list
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

# Print the linked list
example.Print()

# Removing a node
example.popped(5)
example.Print()

# Inserting a new node and where
example.Insert(5,6)
example.Print()

# Showcasing more examples of remove and add
example.popped(2)
example.Print()
example.Insert(2,3)
example.Print()
example.Insert(0,1)
example.Print()
example.Insert(-1,0)
example.Print()