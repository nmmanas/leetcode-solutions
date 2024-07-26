"""
Leetcode link: https://leetcode.com/problems/merge-k-sorted-lists
"""

from typing import List

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
    <question from leetcode>

    Constraints:
    <constraints from leetcode>

    Problem statement (Step 1):
    <problem in own words>

    Input/Output formats (Step 1):
    """
    def solution(self, input1: List[int], input2: int) -> int:
        """
        Pseudo Code (Step 3):

        Analyze Complexity (Step 5):
        
        """
        return -1

def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. first edge case
    """
    test_cases = []
    # 1. 1 pile, hours less than pile size
    test_cases.append({
        'input': {
            'piles': [30,11,23,4,20],
            'h': 6
        }, 'output': 23
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.solution, test_cases)