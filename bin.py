class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def pre_traversal(root):
    if not root:
        return
    print(root.value)
    pre_traversal(root.left)
    pre_traversal(root.right)


def in_traversal(root):
    if not root:
        return
    in_traversal(root.left)
    print(root.value)
    in_traversal(root.right)


def post_traversal(root):
    if not root:
        return
    post_traversal(root.left)
    post_traversal(root.right)
    print(root.value)


def build_tree():
    node = [1, 2, 3, 4, 5, 6, 7]
    root = TreeNode(node[0])
    node_queue = [root]
    index = 1
    while index < len(node):
        node_queue.append(TreeNode(node[index]))
        node_queue[index - 1].left = node_queue[index]
        index += 1
        if index < len(node):
            node_queue.append(TreeNode(node[index]))
            node_queue[index - 2].right = node_queue[index]
            index += 1
    return root


if __name__ == "__main__":
    root = build_tree()
    print("pre_traversal:")
    pre_traversal(root)
    print("in_traversal:")
    in_traversal(root)
    print("post_traversal:")
    post_traversal(root)

# def test_pre_traversal():
#     pass
