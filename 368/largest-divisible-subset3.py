# LeetCode 368. Largest Divisible Subset
# 陣列很多正數，找到最大的 subset 裡面全部可「兩兩」整除
# 想到一個作法，把數字「小到大」排好，再看「函式呼叫函式」全部撒下去試
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        N = len(nums)  # 陣列的長度
        nums.sort()  # 小到大排好
        table = [0]*N  # 用來存「最大的長度」對應的「下一個的長度」
        index = [N]*N  # 用來存「最大的長度」對應的「下一個index」，N代表結束
        @cache  # 函式呼叫函式，用 memo 方法，記錄「試過的參數」避免重覆進入
        def helper(i):  # 請問 nums[i] 開始的「最大的長度」
            if i >= N: return 0  # 超過邊界
            for ii in range(i+1,N):
                if nums[ii]%nums[i]==0:
                    now = helper(ii)
                    if now > table[i]: table[i], index[i] = now, ii
            return table[i] + 1
        nowI = 0  # 最佳的開始點，從 0 開始試
        for i in range(N):
            helper(i)  # 每個格子，都當試看看
            if table[i]>table[nowI]: nowI = i  # 若更好，那就換這裡開始
        ans = []  # 放答案的 list
        while nowI < N:  # 還未「超過邊界」
            ans.append(nums[nowI])  # 把最長的subset逐一塞入 ans
            nowI = index[nowI]  # 下面一位
        return ans

