#binary search tree
class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert(node.right, key)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

    def inorder(self):
        self._inorder(self.root)
        print()  # for a new line after the traversal

    def _inorder(self, node):
        if node:
            self._inorder(node.left)
            print(node.key, end=' ')
            self._inorder(node.right)

# Example usage
if __name__ == "__main__":
    bst = BinarySearchTree()
    keys = [50, 30, 20, 40, 70, 60, 80]

    for key in keys:
        bst.insert(key)

    print("In-order traversal of the BST:")
    bst.inorder()

    search_key = 40
    result = bst.search(search_key)
    if result:
        print(f"\nKey {search_key} found in the BST.")
    else:
        print(f"\nKey {search_key} not found in the BST.")
