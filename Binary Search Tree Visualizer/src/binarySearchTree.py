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
    
    def delete(self,value):
        #if value not found no value is deleted
        if not self.find(value):
            return None
        
        #case 1: no children
        if self.left is None and self.right is None:
            return None
        
        #case 2: one child
        if self.right is None:
            return self.left
        elif self.left is None:
            return self.right

    def _min(self):
        current = self 
        while current.left:
            current = current.left
        return current
    