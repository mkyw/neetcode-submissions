class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # res = 0
        # for n in nums:
        #     res = n ^ res
        # return res
        numSet = set()
        for n in nums:
            if n in numSet:
                numSet.remove(n)
            else:
                numSet.add(n)
        return numSet.pop()
