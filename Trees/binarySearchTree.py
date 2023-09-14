class Node:
    def __init__ (self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__ (self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while(True):
            if temp.value == new_node.value:
                return False
            if temp.value > new_node.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left              
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self,value):
        temp = self.root
        while temp is not None:
            if temp.value > value:
                temp = temp.left
            elif temp.value < value:
                temp = temp.right
            else:
                return True
        return False
                
tree = BinarySearchTree()
tree.insert(47)
tree.insert(21)
tree.insert(76)
tree.insert(18)
tree.insert(27)
tree.insert(52)
tree.insert(82)

print(tree.contains(52))
print(tree.contains(17))
   
