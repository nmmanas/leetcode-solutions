"""
Leetcode link: https://leetcode.com/problems/search-a-2d-matrix
"""

from typing import List

from test import evaluate_test_cases


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # # bruteforce
        # """travel through each row and column, then check for target"""

        # for row in matrix:
        #     for column in row:
        #         if column == target:
        #             return True
                
        # return False

        # # 2 binary searches
        # """
        # given an integer matrix, where each row is sorted ascending 
        # and each row starting value is greater than previous row,
        # return True if the target value is found in the matrix, else False

        # Example:
        #     matrix = [[1,3,5,7],
        #               [10,11,16,20],
        #               [23,30,34,60]]
        #       target = 3
        # 1. Find which row must have the value
        #   a. for each row, get the first element
        #   b. if its same as target, return True
        #   c. if its lower than target,
        #       i. check if current row has it by checking if last element is greater than target
        #       ii. if yes, we found the row
        #       iii. if not, go to rows > current one
        #   d. if its higher than target,
        #       i. check lower rows
        # 2. binary search in current row to see if we have the value
        #   a. take the mid value
        #   b. if its greater than target, check left
        #   c. if its less than target, check right
        #   d. if its same as target, return True
        # 3. if no value found return False (by default)
        # """


        # low = 0
        # high = len(matrix)-1

        # row_to_check = None

        # while low<=high and row_to_check is None:
        #     mid = (low+high)//2
        #     first_of_row = matrix[mid][0]

        #     print(f'{low=},{high=},{first_of_row=},{matrix[mid][-1]=}')

        #     if first_of_row == target:
        #         return True
        #     elif first_of_row < target:
        #         if matrix[mid][-1] >= target:
        #             row_to_check = mid
        #         else:
        #             low = mid + 1
        #     elif first_of_row > target:
        #         high = mid - 1

        # print(f'{row_to_check=}')

        # if row_to_check is not None:
        #     low = 0
        #     high = len(matrix[row_to_check])-1

        #     while low <= high:
        #         mid = (low+high)//2

        #         print('>>>')
        #         print(f'{low=},{high=},{mid=},{matrix[row_to_check][mid]=}')

        #         if matrix[row_to_check][mid] == target:
        #             return True
        #         elif matrix[row_to_check][mid] > target:
        #             high = mid-1
        #         elif matrix[row_to_check][mid] < target:
        #             low = mid + 1

        # return False

        # treat like 1D array
        """
        Since each row is sorted and the last item is less than the 
        first item of next row, what if we consider the rows as a 
        single 1D array.

        1. low = 0, high = rows*columns -1
        2. mid = (low+high)//2
        3. mid_element will be accessed as follows:
            a. divide mid by length of row, get the full answer
            b. row will be above "full answer" + 1
            c. column will be remainder from above
        """

        low = 0
        high = (len(matrix)*len(matrix[0]))-1

        while low <= high:
            mid = (low+high)//2
            mid_element = matrix[mid//len(matrix[0])][mid%len(matrix[0])]

            if mid_element==target:
                return True
            elif mid_element > target:
                high = mid - 1
            elif mid_element < target:
                low = mid + 1

        return False

def load_test_cases():
    """
    1. single row, column, target exists
    2. single row, column, target doesn't exist
    3. multi row, target in first row first, last, random position
    4. multi row, target in last row first, last, random position
    5. multi row, target in random row, first, last, random position
    6. multi row, target doesn't exist, before first, after last, between rows, between values
    7. single row, multi column, target in first, last, random positions
    8. single row, multi column, target doesn't exist
    9. multi row, single column, target in first, last, random rows
    10. multi row, single column, target doesn't exist
    """
    test_cases = []
    # 1. single row, column, target exists
    test_cases.append({
        'input': {
            'matrix': [[100]],
            'target': 100
        }, 'output': True
    })
    # 2. single row, column, target doesn't exist
    test_cases.append({
        'input': {
            'matrix': [[100]],
            'target': 101
        }, 'output': False
    })
    # 3. multi row, target in first row first, last, random position
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25]],
            'target': 1
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25]],
            'target': 5
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25]],
            'target': 2
        }, 'output': True
    })
    # 4. multi row, target in last row first, last, random position
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25]],
            'target': 17
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25]],
            'target': 25
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25]],
            'target': 20
        }, 'output': True
    })
    # 5. multi row, target in random row, first, last, random position
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': 20
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': 25
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': 20
        }, 'output': True
    })
    # 6. multi row, target doesn't exist, before first, after last, between rows, between values
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': -100
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': 50
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': 6
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5],[8,10,12,14],[17,19,20,25],[30,32,34,35]],
            'target': 33
        }, 'output': False
    })
    # 7. single row, multi column, target in first, last, random positions
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5,6,7,8]],
            'target': 1
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5,6,7,8]],
            'target': 2
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5,6,7,8]],
            'target': 8
        }, 'output': True
    })
    # 8. single row, multi column, target doesn't exist
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5,6,7,8]],
            'target': 0
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5,6,7,8]],
            'target': 10
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1,2,4,5,7,8]],
            'target': 6
        }, 'output': False
    })
    # 9. multi row, single column, target in first, last, random rows
    test_cases.append({
        'input': {
            'matrix': [[1],[2],[3],[5],[6]],
            'target': 1
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1],[2],[3],[5],[6]],
            'target': 6
        }, 'output': True
    })
    test_cases.append({
        'input': {
            'matrix': [[1],[2],[3],[5],[6]],
            'target': 5
        }, 'output': True
    })
    # 10. multi row, single column, target doesn't exist
    test_cases.append({
        'input': {
            'matrix': [[1],[2],[3],[5],[6]],
            'target': 0
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1],[2],[3],[5],[6]],
            'target': 8
        }, 'output': False
    })
    test_cases.append({
        'input': {
            'matrix': [[1],[2],[3],[5],[6]],
            'target': 4
        }, 'output': False
    })

    return test_cases

if __name__ == "__main__":
    test_cases = load_test_cases()
    solution = Solution()
    evaluate_test_cases(solution.searchMatrix, test_cases)