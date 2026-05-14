class Solution:
    def maxArea(self, heights: List[int]) -> int:
        a,b = 0, len(heights) - 1
        max_v = 0
        while a < b:
            curr_v = min(heights[a], heights[b]) * (b-a)
            if curr_v > max_v:
                max_v = curr_v
            if heights[b] > heights[a]:
                a += 1
            else:
                b -= 1
        return max_v
