class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        max_l = 0
        l = 0
        most = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            most = max(most, count[s[r]])

            while (r - l + 1) - most > k:
                count[s[l]] -= 1
                l += 1
            
            max_l = max(max_l, r - l + 1)
        
        return max_l