class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            if s[start] != s[end]:
                skip_start = s[start+1:end+1]
                skip_end = s[start:end]

                return (skip_start == skip_start[::-1] or skip_end == skip_end[::-1])

            start += 1
            end -= 1

        return True
        