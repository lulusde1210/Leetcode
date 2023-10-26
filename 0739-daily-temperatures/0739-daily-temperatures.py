class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index = (stack.pop())[0]
                answer[index] = i - index
            
            stack.append([i,temp])
        
        return answer


        # answer = []
        # for i in range(len(temperatures)-1):
        #     count = 0
        #     for j in range(i+1, len(temperatures)):
        #         if temperatures[j] <= temperatures[i]:
        #             count += 1
        #         else:
        #             count += 1
        #             answer.append(count)
        #             break
        #     if count == len(temperatures) - i - 1 and temperatures[i] >= temperatures[j]:
        #         answer.append(0)

        # answer.append(0)
        # return answer
                    

