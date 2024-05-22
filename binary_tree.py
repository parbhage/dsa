#Binary tree
class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert_recursive(node.right, key)

    def inorder_traversal(self):
        self._inorder_traversal_recursive(self.root)
        print()

    def _inorder_traversal_recursive(self, node):
        if node:
            self._inorder_traversal_recursive(node.left)
            print(node.key, end=" ")
            self._inorder_traversal_recursive(node.right)

# Example usage:
tree = BinaryTree()

tree.insert(50)
tree.insert(30)
tree.insert(20)
tree.insert(40)
tree.insert(70)
tree.insert(60)
tree.insert(80)

print("Inorder Traversal:")
tree.inorder_traversal()


