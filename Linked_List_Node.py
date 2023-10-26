class Node(): #Creates a Node instance that contains the nodes value and pointer to the next node
  def __init__(self,value,next_Node = None):
      self.value = value # The Nodes value
      self.nextNode = next_Node # Pointer for the Next Node in the list