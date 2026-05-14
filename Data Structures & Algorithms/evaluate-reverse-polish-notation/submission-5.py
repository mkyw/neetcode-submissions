class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        nums = []
        while tokens:
            i = tokens.pop(0)
            print(i, nums)
            if i == '+':
                nums.append(nums.pop() + nums.pop())
            elif i == '-':
                i = nums.pop()
                j = nums.pop()
                nums.append(j - i)
            elif i == '*':
                nums.append(nums.pop() * nums.pop())
            elif i == '/':
                i = nums.pop()
                j = nums.pop()
                nums.append(int(j / i))
            else:
                nums.append(int(i))
        return nums.pop(0)

# ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
# (10 * (6 / ((9 + 3) * -11)) + 17 + 5