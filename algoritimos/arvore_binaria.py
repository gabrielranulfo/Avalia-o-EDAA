class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def insert(self, value):
        current = self
        while True:
            if value < current.key:
                if current.left is None:
                    current.left = Node(value)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(value)
                    break
                else:
                    current = current.right

    def find_deepest_node(self):
        if self is None:
            return None, 0
        
        queue = [(self, 0)]
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
        stack = []
        current = self
        while True:
            if current is not None:
                stack.append(current)
                current = current.left
            elif stack:
                current = stack.pop()
                print(current.key)
                current = current.right
            else:
                break

    def preorder_traversal(self):
        stack = [self]
        while stack:
            current = stack.pop()
            print(current.key)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    def postorder_traversal(self):
        stack1 = [self]
        stack2 = []
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        while stack2:
            print(stack2.pop().key)

    def find(self, value, comparison_count=0):
        current = self
        while current:
            comparison_count += 1
            if value < current.key:
                current = current.left
            elif value > current.key:
                current = current.right
            else:
                return current.key, comparison_count
        return None, comparison_count
