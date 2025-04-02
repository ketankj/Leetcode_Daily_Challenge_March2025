# You are given a string word and a non-negative integer k.

# Return the total number of substrings of word that contain every vowel ('a', 'e', 'i', 'o', and 'u') at least once and exactly k consonants.

 

# Example 1:

# Input: word = "aeioqq", k = 1

# Output: 0

# Explanation:

# There is no substring with every vowel.

# Example 2:

# Input: word = "aeiou", k = 0

# Output: 1

# Explanation:

# The only substring with every vowel and zero consonants is word[0..4], which is "aeiou".

# Example 3:

# Input: word = "ieaouqqieaouqq", k = 1

# Output: 3

# Explanation:

# The substrings with every vowel and one consonant are:

# word[0..5], which is "ieaouq".
# word[6..11], which is "qieaou".
# word[7..12], which is "ieaouq".

from collections import defaultdict

class Solution:
    def countOfSubstrings(self, word, k):
        def f(k):
            cnt = Counter()
            ans = l = x = 0
            for c in word:
                if c in "aeiou":
                    cnt[c] += 1
                else:
                    x += 1
                while x >= k and len(cnt) == 5:
                    d = word[l]
                    if d in "aeiou":
                        cnt[d] -= 1
                        if cnt[d] == 0:
                            cnt.pop(d)
                    else:
                        x -= 1
                    l += 1
                ans += l
            return ans

        return f(k) - f(k + 1)
    

        


s = Solution()
word = "aeioqq"
k = 1
print(s.countOfSubstrings(word,k))  
