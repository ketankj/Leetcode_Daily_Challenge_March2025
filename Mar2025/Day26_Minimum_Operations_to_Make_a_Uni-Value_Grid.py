# You are given a 2D integer grid of size m x n and an integer x. In one operation, you can add x to or subtract x from any element in the grid.

# A uni-value grid is a grid where all the elements of it are equal.

# Return the minimum number of operations to make the grid uni-value. If it is not possible, return -1.

 

# Example 1:


# Input: grid = [[2,4],[6,8]], x = 2
# Output: 4
# Explanation: We can make every element equal to 4 by doing the following: 
# - Add x to 2 once.
# - Subtract x from 6 once.
# - Subtract x from 8 twice.
# A total of 4 operations were used.
# Example 2:


# Input: grid = [[1,5],[2,3]], x = 1
# Output: 5
# Explanation: We can make every element equal to 3.
# Example 3:


# Input: grid = [[1,2],[3,4]], x = 2
# Output: -1
# Explanation: It is impossible to make every element equal.

class Solution(object):
    def minOperations(self, grid, x):
        # Flatten the grid into a single list
        flat_grid = [num for row in grid for num in row]
        
        # Check if all elements can be transformed to a single value
        remainder = flat_grid[0] % x
        for num in flat_grid:
            if num % x != remainder:
                return -1
        
        # Find the target value using the median
        flat_grid.sort()
        
        # Choose the median
        median = flat_grid[len(flat_grid) // 2]
        
        # Calculate the number of operations
        operations = 0
        for num in flat_grid:
            operations += abs(num - median) // x
        
        return operations
    

        


s = Solution()
grid = [[2,4],[6,8]]
x = 2
print(s.minOperations(grid,x))  
