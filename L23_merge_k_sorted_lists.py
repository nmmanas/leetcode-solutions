"""
Leetcode link: https://leetcode.com/problems/merge-k-sorted-lists
"""

from typing import List, Optional

from datastructures import ListNode
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
    You are given an array of `k` linked-lists `lists`, each linked-list
    is sorted in ascending order. Merge all the linked-lists into 
    one sorted linked-list and return it.

    Constraints:
        `k == lists.length`
        `0 <= k <= 10^4`
        `0 <= lists[i].length <= 500`
        `-104 <= lists[i][j] <= 10^4`
        `lists[i]` is sorted in ascending order.
        The sum of `lists[i].length` will not exceed `10^4`.

    Problem statement (Step 1):
    Given a list of linked-lists, which are sorted in ascending order, merge
    the linked lists in to one sorted linked list and return it

    Input/Output formats (Step 1):
    ** provided by leetcode **
    """
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        """
        Pseudo Code (Step 3):

        Analyze Complexity (Step 5):
        
        """
        return -1

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. multiple lists
    2. all empty lists
    3. one empty list
    4. all single value
    5. one single value
    6. singe and empty lists
    7. leetcode example 1
    8. leetcode example 2
    9. leetcode example 3
    """
    test_cases = []

    # 1. multiple lists
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1,3,5,7,9],[0,2,4,6,8,10]]),
        }, 'output': ListNode.parse_list([0,1,2,3,4,5,6,7,8,9,10])
    })
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1,3,5,7,9],[1,3,5,7,9]]),
        }, 'output': ListNode.parse_list([1,1,3,3,5,5,7,7,9,9])
    })
    # 2. all empty lists
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[],[],[]]),
        }, 'output': ListNode.parse_list([])
    })
    # 3. one empty list
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1,3,5,7,9],[]]),
        }, 'output': ListNode.parse_list([1,3,5,7,9])
    })
    # 4. all single value
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1],[3],[5],[7],[9]]),
        }, 'output': ListNode.parse_list([1,3,5,7,9])
    })
    # 5. one single value
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1,3,7,9],[5]]),
        }, 'output': ListNode.parse_list([1,3,5,7,9])
    })
    # 6. singe and empty lists
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1,3,7,9],[5],[]]),
        }, 'output': ListNode.parse_list([1,3,5,7,9])
    })
    # 7. leetcode example 1
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[1,4,5],[1,3,4],[2,6]]),
        }, 'output': ListNode.parse_list([1,1,2,3,4,4,5,6])
    })
    # 8. leetcode example 2
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([]),
        }, 'output': ListNode.parse_list([])
    })
    # 9. leetcode example 3
    test_cases.append({
        'input': {
            'lists': ListNode.parse_list_of_lists([[]]),
        }, 'output': ListNode.parse_list([])
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.mergeKLists, test_cases)