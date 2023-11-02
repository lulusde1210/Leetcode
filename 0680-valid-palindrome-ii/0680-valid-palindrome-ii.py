class Solution:
    def validPalindrome(self, s: str) -> bool:
        start = 0
        end = len(s)-1

        while start < end:
            if s[start] != s[end]:
                s1 = "".join(s[:start] + s[start+1:])
                s2 = "".join(s[:end] + s[end+1:])

                if s1 != s1[::-1] and s2 != s2[::-1]:
                    return False
                else:
                    return True
            start += 1
            end -= 1

        return True
        