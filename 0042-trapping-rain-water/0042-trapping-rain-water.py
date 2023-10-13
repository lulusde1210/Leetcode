class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = height[l]
        maxR = height[r]
        result = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                maxL = max(maxL, height[l])
                amount = maxL - height[l] 

            else:
                r -= 1
                maxR = max(maxR, height[r])
                amount = maxR - height[r]

            result += amount if amount >0 else 0
            

        return result

        

#######################################################
        # result = 0
        
        # for i in range(1,len(height)-1):
        #     l_max = max(height[:i])
        #     r_max = max(height[i+1:])
        #     amount = min(l_max,r_max) - height[i]
        #     result += amount if amount > 0 else 0
        
        # return result


        