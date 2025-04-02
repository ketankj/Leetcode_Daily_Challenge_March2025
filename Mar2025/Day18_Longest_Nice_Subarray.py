# You are given an array nums consisting of positive integers.

# We call a subarray of nums nice if the bitwise AND of every pair of elements that are in different positions in the subarray is equal to 0.

# Return the length of the longest nice subarray.

# A subarray is a contiguous part of an array.

# Note that subarrays of length 1 are always considered nice.

 

# Example 1:

# Input: nums = [1,3,8,48,10]
# Output: 3
# Explanation: The longest nice subarray is [3,8,48]. This subarray satisfies the conditions:
# - 3 AND 8 = 0.
# - 3 AND 48 = 0.
# - 8 AND 48 = 0.
# It can be proven that no longer nice subarray can be obtained, so we return 3.
# Example 2:

# Input: nums = [3,1,5,11,13]
# Output: 1
# Explanation: The length of the longest nice subarray is 1. Any subarray of length 1 can be chosen.
 

class Solution(object):
    def longestNiceSubarray(self, nums):
        start = 0
        current_and = 0
        max_length = 1  # Any single element is always a nice subarray

        for end in range(len(nums)):
            # While we can add nums[end] without violating the nice subarray condition
            while current_and & nums[end] != 0:
                # Move the start pointer to make the subarray valid again
                current_and ^= nums[start]
                start += 1

            # Add the current element to the current AND
            current_and |= nums[end]

            # Update the maximum length of the nice subarray
            max_length = max(max_length, end - start + 1)

        return max_length
        


s = Solution()
nums = [1,3,8,48,10]
print(s.longestNiceSubarray(nums))  
