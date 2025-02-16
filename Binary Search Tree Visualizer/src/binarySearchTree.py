class TreeNode():
    """
    A class representing a node in a Binary Search Tree (BST).
    Each node contains a value, a left child, and a right child.
    """
    def __init__(self, value):
        """
        Initializes a TreeNode with a given value.
        
        param value: The value to store in the node.
        """
        self.left = None
        self.right = None
        self.value = value

    def insert(self, value):
        """
        Inserts a new value into the BST while maintaining its properties.
        
        param value: The value to insert.
        """
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
        """
        Searches for a value in the BST.
        
        param value: The value to search for.
        return: True if found, False otherwise.
        """
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
        """
        Deletes a node with the given value from the BST.
        
        :param value: The value to delete.
        :return: The updated subtree after deletion.
        """
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
        """
        Finds the node with the smallest value in the subtree.
        
        return: The node with the smallest value.
        """
        current = self 
        while current.left:
            current = current.left
        return current

    def __str__(self):
        """
        Returns an in-order string representation of the BST.
        
        return: A space-separated string of values in sorted order.
        """
        values = []
        self._inorder_traversal(self, values)
        return " ".join(map(str, values))

    def _inorder_traversal(self, node, values):
        """
        Helper method to perform in-order traversal of the BST.
        
        param node: The current node being traversed.
        param values: A list to store node values in sorted order.
        """
        if node is not None:
            self._inorder_traversal(node.left, values)
            values.append(node.value)
            self._inorder_traversal(node.right, values)
