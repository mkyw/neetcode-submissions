class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            digits = [int(d) for d in str(n)]
            sum_digits = 0
            for d in digits:
                sum_digits += pow(d, 2)
            n = sum_digits
            if n in seen:
                return False
            else:
                seen.add(n)
        return True