class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 1:
            return 1
        
        # 'first' represents n-2, 'second' represents n-1
        first, second = 1, 1 
        
        for i in range(2, n + 1):
            current = first + second
            first = second
            second = current
            
        return second