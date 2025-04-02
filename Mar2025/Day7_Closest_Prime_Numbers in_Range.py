# Given two positive integers left and right, find the two integers num1 and num2 such that:

# left <= num1 < num2 <= right .
# Both num1 and num2 are prime numbers.
# num2 - num1 is the minimum amongst all other pairs satisfying the above conditions.
# Return the positive integer array ans = [num1, num2]. If there are multiple pairs satisfying these conditions, return the one with the smallest num1 value. If no such numbers exist, return [-1, -1].

 

# Example 1:

# Input: left = 10, right = 19
# Output: [11,13]
# Explanation: The prime numbers between 10 and 19 are 11, 13, 17, and 19.
# The closest gap between any pair is 2, which can be achieved by [11,13] or [17,19].
# Since 11 is smaller than 17, we return the first pair.
# Example 2:

# Input: left = 4, right = 6
# Output: [-1,-1]
# Explanation: There exists only one prime number in the given range, so the conditions cannot be satisfied.

class Solution(object):
    def sieve(self, n):
        """Returns a boolean list where True means the index is a prime number."""
        is_prime = [True] * (n + 1)
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                for j in range(i * i, n + 1, i):
                    is_prime[j] = False
        
        return is_prime

    def closestPrimes(self, left, right):
        # Generate prime numbers up to 'right' using the sieve
        is_prime = self.sieve(right)
        
        # Extract prime numbers in the range [left, right]
        primes = [i for i in range(left, right + 1) if is_prime[i]]

        if len(primes) < 2:
            return [-1, -1]

        # Find the closest prime pair
        min_diff = float('inf')
        closest_pair = [-1, -1]

        for i in range(len(primes) - 1):
            diff = primes[i + 1] - primes[i]
            if diff < min_diff:
                min_diff = diff
                closest_pair = [primes[i], primes[i + 1]]

        return closest_pair


        


s = Solution()
left = 10
right = 19
print(s.closestPrimes(left,right))  
