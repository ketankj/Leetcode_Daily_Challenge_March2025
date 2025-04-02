# There is a circle of red and blue tiles. You are given an array of integers colors and an integer k. The color of tile i is represented by colors[i]:

# colors[i] == 0 means that tile i is red.
# colors[i] == 1 means that tile i is blue.
# An alternating group is every k contiguous tiles in the circle with alternating colors (each tile in the group except the first and last one has a different color from its left and right tiles).

# Return the number of alternating groups.

# Note that since colors represents a circle, the first and the last tiles are considered to be next to each other.

 

# Example 1:

# Input: colors = [0,1,0,1,0], k = 3

# Output: 3

# Explanation:



# Alternating groups:



# Example 2:

# Input: colors = [0,1,0,0,1,0,1], k = 6

# Output: 2

# Explanation:



# Alternating groups:



# Example 3:

# Input: colors = [1,1,0,1], k = 4

# Output: 0

# Explanation:



class Solution(object):
    def numberOfAlternatingGroups(self, colors, k):
        n = len(colors)
        if k > n:
            return 0  # If k is larger than n, no groups can be formed
        
        # Step 1: Precompute the alternating array
        alternating = [0] * n
        for i in range(n):
            if colors[i] != colors[(i + 1) % n]:
                alternating[i] = 1  # Mark alternating transition
        
        # Step 2: Use a sliding window to check k-length alternating groups
        count = 0
        window_sum = sum(alternating[:k-1])  # Sum of first k-1 elements
        
        for i in range(n):
            # If all k-1 transitions are alternating, it's a valid group
            if window_sum == k-1:
                count += 1
            
            # Slide the window
            window_sum -= alternating[i]  # Remove outgoing element
            window_sum += alternating[(i + k - 1) % n]  # Add incoming element

        return count

        


s = Solution()
colors = [0,1,0,1,0]
k = 3
print(s.numberOfAlternatingGroups(colors,k))  
