class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            mid = (l + r) // 2
            print(nums[l], nums[mid], nums[r])
            if nums[mid] < nums[r]:
                r = mid
                print('new r:', nums[r])
            else:
                l = mid + 1
                print('new l:', nums[l])
        return nums[l]
        


# 1 2 3 4 5 6  => l < m < r

# Right side
# 2 3 4 5 6 1  => r < l < m
# 3 4 5 6 1 2  => r < l < m
# 4 5 6 1 2 3  => r < l < m

# Left side
# 5 6 1 2 3 4  => m < r < l
# 6 1 2 3 4 5  => m < r < l