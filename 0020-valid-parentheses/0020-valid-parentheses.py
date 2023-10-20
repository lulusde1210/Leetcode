class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <= 1:
            return False
        stack = []
        match = {"(":")", "{":"}", "[":"]"}

        for c in s:
            if c in match.keys():
                stack.append(c)
            else:
                if not stack or (stack and match[stack[-1]]) != c:
                    return False
                else:
                    stack.pop()
        
        if len(stack) > 0:
            return False

        return True
                


        

# use a stack to track the characters
# loop through the string, compare each with the top of stack, delete if match
# else return false
# finally return true


