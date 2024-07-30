"""
Leetcode link: https://leetcode.com/problems/powx-n/
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
    Implement pow(x, n), which calculates x raised to the power n (i.e., x^n).

    Example 1:
    Input: x = 2.00000, n = 10
    Output: 1024.00000

    Example 2:
    Input: x = 2.10000, n = 3
    Output: 9.26100

    Example 3:
    Input: x = 2.00000, n = -2
    Output: 0.25000
    Explanation: 2^-2 = 1/2^2 = 1/4 = 0.25

    Constraints:
        `-100.0 < x < 100.0`
        `-2^31 <= n <= (2^31)-1`
        `n` is an integer.
        Either `x` is not zero or `n > 0`.
        `-10^4 <= x^n <= 10^4`

    Problem statement (Step 1):
    Given two numbers raise the first number to the power of second number

    Input/Output formats (Step 1):
    Inputs:
    x: a floating point number, eg: 2.00000
    n: an integer, eg: 10

    Output:
    pow: float which is x raised to the power of n, eg: 1024.00000
    """
    def myPow(self, x: float, n: int) -> float:
        """
        Pseudo Code (Step 3):
        recursively calculate
        1. base case, if n==0, return 1
        2. if n is negative, return 1/pow(x, abs(n))
        3. if n is odd number return x*pow(x, n-1)
        4. if n is even number, reduce problem by 2, return pow(x*x, n/2)
            this is possible because x^n = (x^2)^(n/2)
            example: x^10 = (x^2)^5

        Analyze Complexity (Step 5):
        Time complexity for odd numbers is T(n) = T(n-1) + O(1)
        for even numbers, its T(n) = T(n/2) + O(1)
        Since after an even number, immediate we'd hit an odd number, it can
        also be considered as T(n/2) + O(1)
        Since n is halved at each call, we need to call the function log2^n times
        therefore T(n) = O(logn)

        Space complexity is calculated for the call stack since we don't use
        any additional space relative to the inputs.
        Since we call the function recursively logn times, 
        Space complexity is also O(logn)
        """
        def pow_rec(x, n):
            if not n:
                return 1
            if n < 0:
                return 1 / self.myPow(x, -n)
            if n % 2:
                return x * self.myPow(x, n-1)
            return self.myPow(x*x, n/2)
        
        return round(pow_rec(x, n), 5)

    
def load_test_cases():
    """
    List of identified test cases covering standard, edge cases (Step 2):
    1. leetcode ex 1
    2. leetcode ex 2
    3. leetcode ex 3
    4. x is negative
    5. n is negative
    6. both negative
    7. n is very large
    8. n is very small
    9. x is zero, n > 0
    """
    test_cases = []
    # 1. leetcode ex 1
    test_cases.append({
        'input': {
            'x': 2.00000,
            'n': 10
        }, 'output': 1024.00000
    })
    # 2. leetcode ex 2
    test_cases.append({
        'input': {
            'x': 2.10000,
            'n': 3
        }, 'output': 9.26100
    })
    # 3. leetcode ex 3
    test_cases.append({
        'input': {
            'x': 2.00000,
            'n': -2
        }, 'output': 0.25000
    })
    # 4. x is negative
    test_cases.append({
        'input': {
            'x': -2.00000,
            'n': 10
        }, 'output': 1024.00000
    })
    # 6. both negative
    test_cases.append({
        'input': {
            'x': -2.00000,
            'n': -2
        }, 'output': 0.25000
    })
    # 7. n is very large
    test_cases.append({
        'input': {
            'x': 1.00000,
            'n': pow(2,31)-1
        }, 'output': 1.00000
    })
    # 8. n is very small
    test_cases.append({
        'input': {
            'x': 1.00000,
            'n': pow(-2,31)-1
        }, 'output': 1.00000
    })
    # 9. x is zero, n > 0
    test_cases.append({
        'input': {
            'x': 0.00000,
            'n': 10
        }, 'output': 0.00000
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.myPow, test_cases)