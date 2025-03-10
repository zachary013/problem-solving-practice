class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        temp = temperatures
        n = len(temp)

        ans = n * [0]
        stack = []

        for i, t in enumerate(temp):
            while stack and t > temp[stack[-1]]:
                index = stack.pop()
                ans[index] = i - index

            stack.append(i)

        return ans
        