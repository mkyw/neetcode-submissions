from collections import deque
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                break
            else:
                digits[i] = 0
        if digits[0] == 0:
            digits = deque(digits)
            digits.appendleft(1)
            digits = list(digits)
        return digits