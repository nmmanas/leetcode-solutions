"""
Leetcode link: https://leetcode.com/problems/balanced-binary-tree
"""

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

    Quesion:
    Given a binary tree, determine if it is height-balanced.
    height-balanced = A height-balanced binary tree is a binary tree in which 
    the depth of the two subtrees of every node never differs by more than one.

    Constraints:
        a. The number of nodes in the tree is in the range [0, 5000].
        b. -104 <= Node.val <= 104

    Problem:
    For a given binary tree, check if its height balanced. ie. check if depth of both
    subtrees of all nodes don't differ by more than one.
    """
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Solution:
        1. for each node,
            a. get right max height
            b. get left max height
            c. check if left-right > 1
            d. if yes, immediate break and return False
            e. else return 1+max(left,right)
        2. return True at the end
        """

        """
        Solution breaking out with exception when finding a node with
        unbalanced subtrees
        """
        # def dfs(root):
        #     if root is None:
        #         return 0
            
        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     print(f'{left=},{right=}')

        #     if abs(left-right) > 1:
        #         raise Exception("not balanced")
            
        #     return 1+max(left,right)
        
        # try:
        #     dfs(root)
        # except:
        #     return False
        
        # return True

        """
        Without throwing exception, but completely traversing
        the whole tree, even after encountering a False
        """
        def dfs(root):
            if root is None:
                return [True, 0]
            
            left = dfs(root.left)
            right = dfs(root.right)

            balanced = left[0] and right[0] and abs(left[1]-right[1]) <=1
            
            return [balanced, 1+max(left[1],right[1])]

        
        return dfs(root)[0]


def load_test_cases():
    """
    List of identified test cases covering standard, edge cases:
    1. empty root
    2. single node
    3. balanced both sides
    4. balanced one side has +1 depth
    5. non-balanced root
    6. non-balanced child
    """
    test_cases = []

    # 1. empty root
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(()),
        }, 'output': True
    })


    # 2. single node
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((1)),
        }, 'output': True
    })

    # 3. balanced both sides
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((2,1,3)),
        }, 'output': True
    })

    # 4. balanced one side has +1 depth
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((2,1,(4,3,5))),
        }, 'output': True
    })

    # 5. non-balanced root
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple((((6,4,7),2,5),1,3)),
        }, 'output': False
    })

    # 6. non-balanced child
    test_cases.append({
        'input': {
            'root': TreeNode.parse_tuple(((((None,6,8),4,7),2,5),1,3)),
        }, 'output': False
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.isBalanced, test_cases)