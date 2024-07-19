"""
Leetcode link: https://leetcode.com/problems/diameter-of-binary-tree/
"""

from typing import Optional

from test import evaluate_test_cases

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.tree_to_tuple(self))
    
    def __str__(self):
        return self.__repr__()

    def tree_to_tuple(self, node):
        if not node.left and not node.right:
            return node.val
        left = None
        right = None
        if node.left:
            left = self.tree_to_tuple(node.left)
        if node.right:
            right = self.tree_to_tuple(node.right)
        return (left, node.val, right)
    
    def display_tree(self, space='\t', level=0):
        # print(node.key if node else None, level)

        # If the node is empty
        if self is None:
            print(space*level + '∅')
            return

        # If the node is a leaf
        if self.left is None and self.right is None:
            print(space*level + str(self.val))
            return

        # If the node has children
        self.display_tree(self.right, space, level+1)
        print(space*level + str(self.val))
        self.display_tree(self.left,space, level+1)

class Solution:
    """
    Steps for solving the problem
    1.State the problem in own words. Identify input/output formats
    2.Figure out example input/output values covering edge cases as well
    3.Write plain English pseudo code
    4.Implement, test and fix issues
    5.Analyze complexity and efficiency
    6.Fix complexities and efficiencies, repeat 3-6

    Question:
    Given the root of a binary tree, return the length of the diameter of the tree.

    The diameter of a binary tree is the length of the longest path between any two
    nodes in a tree. This path may or may not pass through the root.

    The length of a path between two nodes is represented by the number of edges between them.

    Problem:
    Given a binary tree, return the maximum length between any 2 nodes.
    """
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        Solution:
        1. for each node, get the max passing lenght
        2. calculate it by taking the max left size and adding with max right size
        3. when passing back, pass the max(left_size, right_size)
        4. keep a max_length = max(max_length, length)
        """

        max_length = 0

        def dfs(root):
            nonlocal max_length

            if root is None:
                return 0

            left_size =  dfs(root.left)
            right_size =  dfs(root.right)

            length = left_size + right_size
            max_length = max(max_length, length)

            return 1 + max(left_size, right_size)
        
        dfs(root)

        return max_length

        

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases:
    1. root node only
    2. root and one child node
    3. root and two children
    4. max length passing through root node
    5. max length not passing through root node
    6. leetcode testcase 1
    7. leetcode testcase 2
    """
    test_cases = []

    # 1. root node only
    test_cases.append({
        'input': {
            'root': parse_tuple((1)),
        }, 'output': 0
    })

    # 2. root and one child node
    test_cases.append({
        'input': {
            'root': parse_tuple((2,1,None)),
        }, 'output': 1
    })

    # 3. root and two children
    test_cases.append({
        'input': {
            'root': parse_tuple((2,1,3)),
        }, 'output': 2
    })

    # 4. max length passing through root node
    test_cases.append({
        'input': {
            'root': parse_tuple(((3,6,None),2,((6,3,4),5,(6,7,8)))),
        }, 'output': 5
    })

    # 5. max length not passing through root node
    test_cases.append({
        'input': {
            'root': parse_tuple((None,2,((6,3,(None,4,(None,8,5))),5,(6,7,8)))),
        }, 'output': 6
    })

    # 6. leetcode testcase 1
    test_cases.append({
        'input': {
            'root': parse_tuple(((4,2,5),1,3)),
        }, 'output': 3
    })

    # 7. leetcode testcase 2
    test_cases.append({
        'input': {
            'root': parse_tuple((2,1,None)),
        }, 'output': 1
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.diameterOfBinaryTree, test_cases)