class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        d = collections.deque()
        res = []
        l=r=0

        while r < len(nums):
            while d and nums[r] > nums[d[-1]]:
                d.pop()
            d.append(r)
            
            if l > d[0]:
                d.popleft()
            
            if r-l+1 == k:
                res.append(nums[d[0]])
                l += 1

            r += 1
        
        return res

