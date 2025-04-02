# Given an integer n, return true if it is possible to represent n as the sum of distinct powers of three. Otherwise, return false.

# An integer y is a power of three if there exists an integer x such that y == 3x.

 

# Example 1:

# Input: n = 12
# Output: true
# Explanation: 12 = 31 + 32
# Example 2:

# Input: n = 91
# Output: true
# Explanation: 91 = 30 + 32 + 34
# Example 3:

# Input: n = 21
# Output: false

class Solution(object):
    def checkPowersOfThree(self, n):
        base3_digits = []
        while n > 0:
            remainder = n % 3
            base3_digits.insert(0, str(remainder))
            n //= 3

        if "2" in base3_digits:
            return False
        else:
            return True
    

        


s = Solution()
a = 12
print(s.checkPowersOfThree(a))  
