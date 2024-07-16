"""
Leetcode link: https://leetcode.com/problems/koko-eating-bananas
"""

from typing import List
import math

from test import evaluate_test_cases


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        given list of integers depicting piles of bananas, and h
        which is the number of hours available, find the minimum
        speed "k" per hour the bananas in each pile should be eaten

        Constraints:

            1 <= piles.length <= 104
            piles.length <= h <= 109
            1 <= piles[i] <= 109

        piles: list of integers - depicting piles of bananas
        h: number of hours the monkey has

        return:
        speed: minimum eating speed necessary per hour

        Example:
            Input: piles = [3,6,7,11], h = 8
            Output: 4
        """
        
        # # bruteforce
        # """
        # what is the number the can divide each of the pile contents
        # by exactly 'h' times?
        # 1. divide hours by length of piles = x
        # 2. divide each pile by x and count hours needed
        # 3. if its greater than h, increment x and try again

        # eg:
        #     - divide hours by length of piles = 2
        #     - divide each pile by 2 and count units = 15
        #     - increase 2 by one and check again = 3
        #     - divide each pile by 3 and count units  = 9
        #     - increase 2 by one and check again = 4
        #     - divide each pile by 4 and count units = 8
        # """
        # speed = max(1, len(piles)//h)

        # while True:
        #     tmp_h = 0
        #     for p in piles:
        #         tmp_h += math.ceil(p/speed)

        #     if tmp_h <= h:
        #         return speed
            
        #     speed += 1

        # binary search
        """
        As per the test cases, it seems the min speed is between
        1 and the highest element in the pile

        1. check between 1 and max(piles)
        2. for each mid value, check the total hours it'd take
            to eat in that speed
        3. if the total hours is greater than given hour, then we need
            to look at higher speeds, ie. low = mid+1
        4. if the total hours is less than or equal to given hour, 
            then we may have the answer, but we don't know if its 
            the minimum speed, so we include the current speed and 
            check the lower speeds, ie. high = mid (not mid+1 since
            we need to include current speed as well)
        """

        low = 1
        high = max(piles)

        while low < high:
            tmp_h = 0
            speed = (low+high)//2

            for p in piles:
                tmp_h += math.ceil(p/speed)

            if tmp_h <= h:
                high = speed
            elif tmp_h > h:
                low = speed + 1

        return high

def load_test_cases():
    """
    1. 1 pile, hours less than pile size
    2. 1 pile, hours greater than pile size
    3. 1 pile, hours equal to pile size
    4. multiple piles, hours same as pile length
    5. multiple piles, hours greater than pile length
    6. multiple piles, hours less than min pile size
    7. multiple piles, hours equal to min pile size
    8. multiple piles, hours between min,max pile sizes
    9. multiple piles, hours equal to max pile size
    10. multiple piles, hours greater than max pile size
    11. leetcode test case 1
    12. leetcode test case 2
    13. leetcode test case 3
    """
    test_cases = []
    # 1. 1 pile, hours less than pile size
    test_cases.append({
        'input': {
            'piles': [5],
            'h': 4
        }, 'output': 2
    })
    # 2. 1 pile, hours greater than pile size
    test_cases.append({
        'input': {
            'piles': [5],
            'h': 6
        }, 'output': 1
    })
    # 3. 1 pile, hours equal to pile size
    test_cases.append({
        'input': {
            'piles': [5],
            'h': 5
        }, 'output': 1
    })
    # 4. multiple piles, hours same as pile length
    test_cases.append({
        'input': {
            'piles': [3,6,7,11],
            'h': 4
        }, 'output': 11
    })
    # 5. multiple piles, hours greater than pile length
    test_cases.append({
        'input': {
            'piles': [3,6,7,11],
            'h': 6
        }, 'output': 6
    })
    # 6. multiple piles, hours less than min pile size
    test_cases.append({
        'input': {
            'piles': [9,6,7,11],
            'h': 5
        }, 'output': 9
    })
    # 7. multiple piles, hours equal to min pile size
    test_cases.append({
        'input': {
            'piles': [9,6,7,11],
            'h': 6
        }, 'output': 7
    })
    # 8. multiple piles, hours between min,max pile sizes
    test_cases.append({
        'input': {
            'piles': [9,6,7,11],
            'h': 8
        }, 'output': 6
    })
    # 9. multiple piles, hours equal to max pile size
    test_cases.append({
        'input': {
            'piles': [9,6,7,11],
            'h': 11
        }, 'output': 4
    })
    # 10. multiple piles, hours greater than max pile size
    test_cases.append({
        'input': {
            'piles': [9,6,7,11],
            'h': 15
        }, 'output': 3
    })
    # 11. leetcode test case 1
    test_cases.append({
        'input': {
            'piles': [3,6,7,11],
            'h': 8
        }, 'output': 4
    })
    # 12. leetcode test case 2
    test_cases.append({
        'input': {
            'piles': [30,11,23,4,20],
            'h': 5
        }, 'output': 30
    })
    # 13. leetcode test case 3
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
    evaluate_test_cases(solution.minEatingSpeed, test_cases)