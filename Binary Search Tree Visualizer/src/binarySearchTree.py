class TreeNode():
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = TreeNode(value)
            else: 
                self.right.insert(value)
                
    def find(self, value):
        if value < self.value:
            if self.left is None:
                return False
            return self.left.find(value)
        elif value > self.value:
            if self.right is None:
                return False
            return self.right.find(value)
        else:
            return True
    
    def delete(self, value):
    #If value not found, return self unchanged
        if value < self.value:
            if self.left:
                self.left = self.left.delete(value)
        elif value > self.value:
            if self.right:
                self.right = self.right.delete(value)
        else:
            # Case 1: No children
            if self.left is None and self.right is None:
                return None

            # Case 2: One child
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            #Case 3: Two children
            successor = self.right._min() #Find in-order successor (smallest value in right subtree)
            self.value = successor.value  #Copy the successor value
            self.right = self.right.delete(successor.value)  #Delete the successor

        return self  #Return the updated tree reference

    def _min(self):
        current = self 
        while current.left:
            current = current.left
        return current

    # In-order traversal method to print the tree
    def __str__(self):
        values = []
        self._inorder_traversal(self, values)
        return " ".join(map(str, values))

    # Helper method for in-order traversal
    def _inorder_traversal(self, node, values):
        if node is not None:
            self._inorder_traversal(node.left, values)
            values.append(node.value)
            self._inorder_traversal(node.right, values)
