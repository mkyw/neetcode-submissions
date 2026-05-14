class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1:
            sum_digits = 0
            while n:
                digit = n % 10
                digit = digit ** 2
                sum_digits += digit
                n = n // 10
            if sum_digits in seen:
                return False
            else:
                seen.add(sum_digits)
                n = sum_digits
        return True