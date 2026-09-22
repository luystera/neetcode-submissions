class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n):
            current = temperatures[i]
            while (stack and temperatures[stack[-1]] < current):
                index = stack.pop()
                res[index] = i - index
            stack.append(i)
        
        return res