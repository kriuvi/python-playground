class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.data = val
        self.left = left
        self.right = right

    def __repr__(self):
        if not self.left and not self.right:
            return "TreeNode({0})".format(self.data)
        elif not self.right:
            return "TreeNode({0}, {1})".format(self.data, self.left)
        else:
            return "TreeNode({0}, {1}, {2})".format(self.data, self.left, self.right)

class BinaryTree:
    def __init__(self, node=None):
        self.root = node


def search(val, node):
    if node is None or node.data == val:
        return node
    elif node.data > val:
        search(val, node.right)
    else:
        search(val, node.left)


def insert(value, node):
    if value < node.data:
        if node.left is None:
            node.left = TreeNode(value)
        else:
            insert(value, node.left)
    if value > node.data:
        # If the right child does not exist, we want to insert​
        # ​ the value as the right child:​
        if node.right is None:
            node.right = TreeNode(value)
        else:
            insert(value, node.right)


def traverse_and_print(node):
    if not node:
        return
    traverse_and_print(node.left)
    print(node.data)
    traverse_and_print(node.right)


def delete(val, node):
    if node is None:
        return None
    elif val < node.data:
        node.left = delete(val, node.left)
        return node
    elif val > node.data:
        node.right = delete(val, node.right)
        return node
    elif val == node.data:
        if not node.left:
            return node.right
        elif not node.right:
            return node.left
        else:
            node.right = lift(node.right, node)
            return node


def lift(node, node_to_delete):
    if node.left:
        node.left = lift(node.left, node_to_delete)
        return node
    else:
        node_to_delete.value = node.value
        return node.right
