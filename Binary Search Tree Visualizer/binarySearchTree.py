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
                
tree = TreeNode(5)
tree.insert(5)
tree.insert(4)
tree.insert(3)
tree.insert(7)
