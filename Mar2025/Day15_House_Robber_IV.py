# There are several consecutive houses along a street, each of which has some money inside. There is also a robber, who wants to steal money from the homes, but he refuses to steal from adjacent homes.

# The capability of the robber is the maximum amount of money he steals from one house of all the houses he robbed.

# You are given an integer array nums representing how much money is stashed in each house. More formally, the ith house from the left has nums[i] dollars.

# You are also given an integer k, representing the minimum number of houses the robber will steal from. It is always possible to steal at least k houses.

# Return the minimum capability of the robber out of all the possible ways to steal at least k houses.

 

# Example 1:

# Input: nums = [2,3,5,9], k = 2
# Output: 5
# Explanation: 
# There are three ways to rob at least 2 houses:
# - Rob the houses at indices 0 and 2. Capability is max(nums[0], nums[2]) = 5.
# - Rob the houses at indices 0 and 3. Capability is max(nums[0], nums[3]) = 9.
# - Rob the houses at indices 1 and 3. Capability is max(nums[1], nums[3]) = 9.
# Therefore, we return min(5, 9, 9) = 5.
# Example 2:

# Input: nums = [2,7,9,3,1], k = 2
# Output: 2
# Explanation: There are 7 ways to rob the houses. The way which leads to minimum capability is to rob the house at index 0 and 4. Return max(nums[0], nums[4]) = 2.
 

class Solution(object):
    def minCapability(self, nums, k):
        def canRob(cap):
            count = 0
            i = 0
            while i < len(nums):
                if nums[i] <= cap:
                    count += 1
                    i += 2  # Skip the adjacent house.
                else:
                    i += 1
            return count >= k

        # The answer must be between the smallest and largest amount in nums.
        left, right = min(nums), max(nums)
        
        while left <= right:
            mid = (left + right) // 2
            if canRob(mid):
                right = mid - 1  # Try to lower the capability.
            else:
                left = mid + 1   # Increase the candidate capability.
        
        # left will be the minimum capability that works.
        return left
    

        


s = Solution()
nums = [2,3,5,9]
k = 2
print(s.minCapability(nums,k))  
