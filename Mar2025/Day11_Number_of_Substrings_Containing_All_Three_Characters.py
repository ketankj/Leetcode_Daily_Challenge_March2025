# Given a string s consisting only of characters a, b and c.

# Return the number of substrings containing at least one occurrence of all these characters a, b and c.

 

# Example 1:

# Input: s = "abcabc"
# Output: 10
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 
# Example 2:

# Input: s = "aaacb"
# Output: 3
# Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 
# Example 3:

# Input: s = "abc"
# Output: 1

class Solution(object):
    def numberOfSubstrings(self, s):
        n = len(s)
        result = 0
        char_count = {'a': 0, 'b': 0, 'c': 0}
        start = 0

        for end in range(n):
            # Add the current character to the count
            char_count[s[end]] += 1
            
            # Check if the window contains at least one of each 'a', 'b', and 'c'
            while all(char_count[char] > 0 for char in 'abc'):
                # If the current window contains all characters, count the substrings
                result += n - end  # All substrings starting at 'start' and ending from 'end' to 'n-1'
                
                # Shrink the window from the left
                char_count[s[start]] -= 1
                start += 1

        return result
    

        


s = Solution()
a = "abcabc"
print(s.numberOfSubstrings(a))  
