"""
Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: Starting with any positive integer,
replace the number by the sum of the squares of its digits,
and repeat the process until the number equals 1 (where it will stay),
or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example:

Input: 19
Output: true
Explanation:
12 + 92 = 82
82 + 22 = 68
62 + 82 = 100
12 + 02 + 02 = 1
"""
class Solution(object):
    def isHappy(n):
        """
        :type n: int
        :rtype: bool
        """
        history = []
        n_temp, n_sum = 0, 0
        while n_sum != 1:
            n_sum = 0
            for n_part in str(n):
                n_sum += int(n_part)**2
            if n_sum == 1:
                return True
            if n_sum in history:
                return False
            n = n_sum
            history.append(n_sum)


for test_n in range(20):
    result = Solution.isHappy(test_n)
    print(f'{test_n} result is {result}')
