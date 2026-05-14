class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        max_l = 0
        l = 0
        map_s = {}

        for r in range(len(s)):
            if s[r] in map_s:
                l = max(map_s[s[r]] + 1, l)
            map_s[s[r]] = r
            max_l = max(max_l, r - l + 1)
        return max_l
        