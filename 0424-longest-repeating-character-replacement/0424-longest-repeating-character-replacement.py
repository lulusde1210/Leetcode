class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
         l,r = 0,0
         longest = 0
         count = defaultdict(int)

         for r in range(len(s)):
             count[s[r]] += 1
             most = max(count.values())
             sLength = r-l+1

             if sLength - most <= k:
                 longest = max(longest,sLength)
             else:
                 count[s[l]] -= 1
                 l += 1

         return longest
