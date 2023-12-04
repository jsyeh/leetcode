class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = ""
        N = len(num)
        for i in range(N-2):
            if num[i] == num[i+1] and num[i+1] == num[i+2]:
                if ans == "" or ans[0]<num[i]:
                    ans = num[i]*3
        return ans
