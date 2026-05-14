class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tot = 1
        numZeros = 0
        z_index = -1
        prodList = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] == 0:
                numZeros += 1
                z_index = i
            else:
                tot *= nums[i]
        
        if numZeros > 1:
            return prodList
        if numZeros == 1:
            prodList[z_index] = tot
            return prodList
        
        for i in range(len(nums)):
            prodList[i] = tot // nums[i]
        
        return prodList
            