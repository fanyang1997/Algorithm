from typing import *


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryTreeAlg:
    def __init__(self, root: TreeNode):
        self.root = root

    def pre_traversal(self):
        root = self.root
        if not root:
            return
        print(root.value)
        self.pre_traversal(root.left)
        self.pre_traversal(root.right)

    def in_traversal(self):
        root = self.root
        if not root:
            return
        self.in_traversal(root.left)
        print(root.value)
        self.in_traversal(root.right)

    def post_traversal(self):
        root = self.root
        if not root:
            return
        self.post_traversal(root.left)
        self.post_traversal(root.right)
        print(root.value)

    def pre_traversal_stack(self) -> List[int]:
        # [1, 2, 3, 4, 5, 6, 7]
        # stack = [1]
        root = self.root
        if not root:
            return
        stack = [root]
        result = []
        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return result

    def in_traversal_stack(self) -> List[int]:
        pass

    def post_traversal_stack(self) -> List[int]:
        pass

    def level_order(self) -> List[List[int]]:
        root = self.root
        if not root:
            return
        result = []
        queue = [root]
        while queue:
            level = []
            for _ in range(len(queue)): # [3, 4, 5]
                node = queue.pop(0)
                level.append(node.value)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level)
        return result

    def inverse_binary_tree(self) -> TreeNode:
        root = self.root
        if not root:
            return
        left = self.inverse_binary_tree(root.left)
        right = self.inverse_binary_tree(root.right)
        root.left, root.right = right, left
        return root

    def max_depth_binary_tree(self) -> int:
        root = self.root
        if not root:
            return 0
        return max(self.max_depth_binary_tree(root.left), self.max_depth_binary_tree(root.right)) + 1

    def right_view_binary_tree(self) -> List[int]:
        if not root:
            return []
        result = []
        result.append(root.value)
        self.right_view_binary_tree_helper(root.right, result, 1)
        return result

    def right_view_binary_tree_helper(self, result, depth) -> None:
        if not root:
            return
        if depth == len(result):
            result.append(root.value)
        self.right_view_binary_tree_helper(root.right, result, depth + 1)

        


def build_tree():
    node = [1, 2, 3, 4, 5, 6, 7]
    # node = [4, 2, 7, 1, 3, 6, 9]
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


def print_tree(root):
    if not root:
        return
    print(root.value)
    print_tree(root.left)
    print_tree(root.right)


if __name__ == "__main__":
    # root = build_tree()
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)
    bta = BinaryTreeAlg(root)
    # print("pre_traversal:")
    # bta.pre_traversal(root)
    # print("in_traversal:")
    # bta.in_traversal(root)
    # print("post_traversal:")
    # bta.post_traversal(root)
    # print("inverse_binery_tree:")
    # root = bta.inverse_binary_tree(root)
    # print_tree(root)
    # print("pre_traversal:")
    # bta.pre_traversal(root)

    pre_order_test_case = {
        "[]": [],
        "[1]": [1],
        "[1, 2]": [1, 2],
        "[1, 2, 3]": [1, 3, 2]
    }

    in_order_test_case = {
        "[]": [],
        "[1]": [1],
        "[1, 2]": [2, 1],
        "[1, 2, 3]": [2, 1, 3]
    }

    # for key, value in pre_order_test_case.items():
    #     print(key, ":", value)
    #     assert bta.pre_traversal_stack(root) == value
    bta.level_order()