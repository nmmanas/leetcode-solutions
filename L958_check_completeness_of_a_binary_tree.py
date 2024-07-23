"""
Leetcode link: https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""

from collections import defaultdict
from typing import Optional

from datastructures import TreeNode
from test import evaluate_test_cases


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
    Given the root of a binary tree, determine if it is a complete binary tree.

    In a complete binary tree, every level, except possibly the last, is completely filled, 
    and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes 
    inclusive at the last level h.

    Constraints:
        * The number of nodes in the tree is in the range [1, 100].
        * 1 <= Node.val <= 1000

    Problem statement (Step 1):
    Check if the given binary tree is a complete binary tree. A binary tree is considered complete, if
    all the levels are complete except the last level. Last level can be incomplete provided the filled
    nodes are skewing to the left as possible.

    Input/Output formats (Step 1):
    """
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        """
        Pseudo Code (Step 3):
        DFS
        1. for each node check if the left and right are complete
        2. for last level, check if the nodes are filled from the left side

        Analyze Complexity (Step 5):
        * time complexity is O(2n) => O(n)
        * space complexity is O(n)
        """

        levels = defaultdict(list)

        def dfs(root, level=1):
            levels[level].append(root)

            if root is None:
                return []

            dfs(root.left, level+1)
            dfs(root.right, level+1)

        dfs(root)

        
        found = False
        for _,v in levels.items():
            for e in v:
                if found and e is not None:
                    return False
                if e is None:
                    found = True

        return True

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. root only
    2. 2 levels, complete
    3. 2 levels, partially complete
    4. 2 levels, incomplete
    5. 3 levels, complete
    6. 3 levels, partially complete, missing 1 node
    7. 3 levels, partially complete, missing both nodes of right
    8. 3 levels, partially complete, only 1 node in left
    9. 3 levels, incomplete, missing right-left
    10. 3 levels, incomplete, missing left-right
    11. 3 levels, incomplete, missing left-left
    12. 3 levels, incomplete, missing left-left, also right-both
    13. 3 levels, incomplete, missing left-both
    14. 3 levels, incomplete, missing left
    """
    test_cases = []

    # 1. root only
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((1)),
        }, 'output': True
    })

    # 2. 2 levels, complete
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((2,1,3)),
        }, 'output': True
    })

    # 3. 2 levels, partially complete
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((2,1,None)),
        }, 'output': True
    })

    # 4. 2 levels, incomplete
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((None,1,3)),
        }, 'output': False
    })

    # 5. 3 levels, complete
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,5),1,(6,3,7))),
        }, 'output': True
    })

    # 6. 3 levels, partially complete, missing 1 node
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,5),1,(6,3,None))),
        }, 'output': True
    })

    # 7. 3 levels, partially complete, missing both nodes of right
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,5),1,3)),
        }, 'output': True
    })

    # 8. 3 levels, partially complete, only 1 node in left
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,None ),1,3)),
        }, 'output': True
    })

    # 9. 3 levels, incomplete, missing right-left
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,5),1,(None,3,7))),
        }, 'output': False
    })

    # 10. 3 levels, incomplete, missing left-right
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,None),1,(6,3,7))),
        }, 'output': False
    })

    # 11. 3 levels, incomplete, missing left-left
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((None,2,5),1,(6,3,7))),
        }, 'output': False
    })

    # 12. 3 levels, incomplete, missing left-left, also right-both
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((None,2,5),1,3)),
        }, 'output': False
    })

    # 13. 3 levels, incomplete, missing left-both
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((2,1,(6,3,7))),
        }, 'output': False
    })

    # 14. 3 levels, incomplete, missing left
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((None,1,(6,3,7))),
        }, 'output': False
    })


    # 14. leetcode testcase
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((4,2,None),1,(6,3,None))),
        }, 'output': False
    })



    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.isCompleteTree, test_cases)