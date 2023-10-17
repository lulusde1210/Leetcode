class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
         longest = 0
         i,j = 0,0
         hash = {}

         while j < len(s):
             if s[j] in hash and hash[s[j]] >= i:
                 i = hash[s[j]] + 1

             longest = max(longest, len(s[i:j+1]))
             hash[s[j]] = j
             j += 1

         return longest

