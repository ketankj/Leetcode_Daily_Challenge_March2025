# You have k bags. You are given a 0-indexed integer array weights where weights[i] is the weight of the ith marble. You are also given the integer k.

# Divide the marbles into the k bags according to the following rules:

# No bag is empty.
# If the ith marble and jth marble are in a bag, then all marbles with an index between the ith and jth indices should also be in that same bag.
# If a bag consists of all the marbles with an index from i to j inclusively, then the cost of the bag is weights[i] + weights[j].
# The score after distributing the marbles is the sum of the costs of all the k bags.

# Return the difference between the maximum and minimum scores among marble distributions.

 

# Example 1:

# Input: weights = [1,3,5,1], k = 2
# Output: 4
# Explanation: 
# The distribution [1],[3,5,1] results in the minimal score of (1+1) + (3+1) = 6. 
# The distribution [1,3],[5,1], results in the maximal score of (1+3) + (5+1) = 10. 
# Thus, we return their difference 10 - 6 = 4.
# Example 2:

# Input: weights = [1, 3], k = 2
# Output: 0
# Explanation: The only distribution possible is [1],[3]. 
# Since both the maximal and minimal score are the same, we return 0.

class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        # Edge case: If k is 1, the difference is always 0 because there's only one way to divide
        if k == 1:
            return 0
        
        # Calculate the pairwise sums between adjacent marbles
        pairwise_costs = []
        for i in range(len(weights) - 1):
            pairwise_costs.append(weights[i] + weights[i + 1])

        # Sort the pairwise sums in ascending order
        pairwise_costs.sort()

        # Maximize score by selecting the highest k-1 pairwise costs
        max_score = sum(pairwise_costs[-(k-1):])

        # Minimize score by selecting the lowest k-1 pairwise costs
        min_score = sum(pairwise_costs[:(k-1)])

        # The result is the difference between the maximum and minimum scores
        return max_score - min_score

        


s = Solution()
weights = [1,3,5,1]
k = 2
print(s.putMarbles(weights,k))  
