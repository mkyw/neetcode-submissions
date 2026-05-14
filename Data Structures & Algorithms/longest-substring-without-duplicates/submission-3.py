class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        a = 0
        b = 1
        max_l = 1
        ss = s[a]
        while b < len(s):
            if s[b] not in ss:
                ss += s[b]
                b += 1
            else:
                while s[b] in ss:
                    ss = ss[1:]
                    a += 1
                ss += s[b]
                b += 1
            max_l = max(max_l, len(ss))
        return max_l