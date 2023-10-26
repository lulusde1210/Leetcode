class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
            pairs = [(p,s) for p, s in zip(position, speed)]
            pairs.sort(reverse=True)

            stack = [pairs[0]]

            for p,s in pairs[1:]:
                time = (target - p)/s
                if stack and time > (target-stack[-1][0])/stack[-1][1]:
                    stack.append((p,s))

        
            return len(stack)


# [(10, 2), (8, 4), (5, 1), (3, 3), (0, 1)]
#    1.       1.      7.      3.      12
# [(10,2),(5,1),(0,12)]

# [(4,1),(2,2),(0,4)]
#   96.   49.    25
# [(4,1),]