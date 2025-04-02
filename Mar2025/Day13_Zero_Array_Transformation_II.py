# You are given an integer array nums of length n and a 2D array queries where queries[i] = [li, ri, vali].

# Each queries[i] represents the following action on nums:

# Decrement the value at each index in the range [li, ri] in nums by at most vali.
# The amount by which each value is decremented can be chosen independently for each index.
# A Zero Array is an array with all its elements equal to 0.

# Return the minimum possible non-negative value of k, such that after processing the first k queries in sequence, nums becomes a Zero Array. If no such k exists, return -1.

 

# Example 1:

# Input: nums = [2,0,2], queries = [[0,2,1],[0,2,1],[1,1,3]]

# Output: 2

# Explanation:

# For i = 0 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [1, 0, 1].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 0, 1] respectively.
# The array will become [0, 0, 0], which is a Zero Array. Therefore, the minimum value of k is 2.
# Example 2:

# Input: nums = [4,3,2,1], queries = [[1,3,2],[0,2,1]]

# Output: -1

# Explanation:

# For i = 0 (l = 1, r = 3, val = 2):
# Decrement values at indices [1, 2, 3] by [2, 2, 1] respectively.
# The array will become [4, 1, 0, 0].
# For i = 1 (l = 0, r = 2, val = 1):
# Decrement values at indices [0, 1, 2] by [1, 1, 0] respectively.
# The array will become [3, 0, 0, 0], which is not a Zero Array.

class Solution(object):
    def minZeroArray(self, nums, queries):
        n = len(nums)
        
        # Function to check if `nums` can become zero with first `k` queries
        def can_zero(k):
            diff = [0] * (n + 1)
            temp_nums = nums[:]  # Copy of original nums to simulate updates

            for i in range(k):
                l, r, val = queries[i]
                diff[l] -= val
                diff[r + 1] += val  # Mark end of decrement range

            # Apply the difference array
            curr = 0
            for i in range(n):
                curr += diff[i]
                temp_nums[i] = max(0, temp_nums[i] + curr)

            return all(x == 0 for x in temp_nums)  # Check if zero array

        # Edge case: If nums is already zero, return 0
        if all(x == 0 for x in nums):
            return 0

        # Binary Search to find the smallest `k`
        low, high, result = 1, len(queries), -1
        while low <= high:
            mid = (low + high) // 2
            if can_zero(mid):
                result = mid  # Found a possible answer, try to minimize
                high = mid - 1
            else:
                low = mid + 1

        return result
        


s = Solution()
nums = [2,0,2]
queries = [[0,2,1],[0,2,1],[1,1,3]]
print(s.minZeroArray(nums,queries))  
