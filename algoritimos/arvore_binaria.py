class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.key:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)

    def find_deepest_node(self, height=0):
        if self is None:
            return None, height
        
        queue = [(self, height)]
        deepest_node = None
        max_height = 0

        while queue:
            node, height = queue.pop(0)
            
            if height > max_height:
                max_height = height
                deepest_node = node

            if node.left:
                queue.append((node.left, height + 1))
                
            if node.right:
                queue.append((node.right, height + 1))

        return [deepest_node, max_height]


    def inorder_traversal(self):
        if self.left:
            self.left.inorder_traversal()
        print(self.key)
        if self.right:
            self.right.inorder_traversal()

    def preorder_traversal(self):
        print(self.key)
        if self.left:
            self.left.preorder_traversal()
        if self.right:
            self.right.preorder_traversal()

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.key)

    def find(self, value, comparison_count):
        if value < self.key:
            comparison_count = comparison_count + 1
            if self.left is None:
                return [False, comparison_count + 1]
            else:
                return self.left.find(value, comparison_count + 1)
        elif value > self.key:
            comparison_count = comparison_count + 2
            if self.right is None:
                return [False, comparison_count + 1]
            else:
                return self.right.find(value, comparison_count + 1)
        else:
            return [self.key, comparison_count + 2]
        
        # Time complexity: Best case O(log N), worst case (n)
        # auxiliary space: O(1)
    
    