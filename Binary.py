class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def insert(self, data):
        """Insert a new node into the binary search tree."""
        if data < self.data:
            if self.left is None:
                self.left = Node(data)
            else:
                self.left.insert(data)
        elif data > self.data:
            if self.right is None:
                self.right = Node(data)
            else:
                self.right.insert(data)
        # If data == self.data, do nothing (no duplicates)

    def inorder(self):
        """In-order traversal: returns all elements in sorted order."""
        elements = []
        if self.left:
            elements += self.left.inorder()
        elements.append(self.data)
        if self.right:
            elements += self.right.inorder()
        return elements

    def __str__(self):
        return " ".join(str(x) for x in self.inorder())


# Example usage
if __name__ == "__main__":
    root = Node(12)
    for value in [6, 14, 3]:
        root.insert(value)

    print("In-order Traversal:", root)
