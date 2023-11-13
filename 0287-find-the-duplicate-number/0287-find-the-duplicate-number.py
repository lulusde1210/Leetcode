class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()
        temp = None

        for num in nums:
            if num == temp:
                return num
            temp = num

        

        