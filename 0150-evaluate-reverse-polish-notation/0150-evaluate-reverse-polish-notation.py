class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for token in tokens:
            if token in {"+","-","*","/"}:
                num1 = stack.pop()
                num2 = stack.pop()
                if token == "+":
                    result = num1 + num2
                elif token == "-":
                    result = num2 - num1
                elif token == "*":
                    result = num1 * num2
                else:
                    result = int(num2 / num1)
                stack.append(result)
            else:
                stack.append(int(token))
        
        return stack[-1]


#stack = [] store numbers
#go through the tokens, if token is a number add to stack
#if token is an operator, take the last two numbers of the stack , go the operation
#pop the two numbers and add the result to stack
#keep looping. add numbers or do the operations, 
#return the top of stack

        