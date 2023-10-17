class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

##########use a hash set#################
        letter_set = set()
        i,j = 0,0
        longest = 0

        while j < len(s):
            while s[j] in letter_set:
                    letter_set.remove(s[i])
                    i += 1
            longest = max(longest, j-i+1)
            letter_set.add(s[j])
            j+=1
                
        
        return longest




###########use a hash map#################
        #  longest = 0
        #  i,j = 0,0
        #  hash = {}

        #  while j < len(s):
        #      if s[j] in hash and hash[s[j]] >= i:
        #          i = hash[s[j]] + 1

        #      longest = max(longest, len(s[i:j+1]))
        #      hash[s[j]] = j
        #      j += 1

        #  return longest

