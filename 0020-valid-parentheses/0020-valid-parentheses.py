class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {"(":")", "{":"}", "[":"]"}

        for c in s:
            if c in match:
                stack.append(c)
            else:
                if not stack or match[stack[-1]] != c:
                    return False
                stack.pop()
        
        return len(stack) == 0
                


        

# use a stack to track the characters
# loop through the string, compare each with the top of stack, delete if match
# else return false
# finally return true


