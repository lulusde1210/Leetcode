class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backTrack(openP, closeP):
            if openP == closeP == n:
                res.append("".join(stack))
                return
            
            if openP < n:
                stack.append("(")
                backTrack(openP+1, closeP)
                stack.pop()
            
            if closeP < openP:
                stack.append(")")
                backTrack(openP, closeP+1)
                stack.pop()
        
        backTrack(0,0)
        return res

        