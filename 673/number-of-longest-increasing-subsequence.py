class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        N = len(nums)
        table = [0]*N # table[i] 包含 nums[i] 的 LIS 的長度
        count = [0]*N # count[i] 包含 nums[i] 的 LIS 的數量

        maxLIS = 0
        for i in range(N):
            table[i] = 1
            count[i] = 1
            for k in range(i):
                if nums[k] < nums[i] and table[k]+1 > table[i]:
                # 符合 LIS 的條件，而且更長，就整組更新
                    table[i] = table[k] + 1
                    count[i] = count[k]
                elif nums[k] < nums[i] and table[k]+1 == table[i]:
                # 符合 LIS 的條件，且一樣長，就增加count[i]
                    count[i] += count[k]
            if table[i] > maxLIS: # 順手比對，找出 maxLIS 的值
                maxLIS = table[i]

        ans = 0 # 含有 maxLIS 的 count[i] 總合
        for i in range(N):
            if table[i] == maxLIS: # nums[i] 符合 maxLIS 的長度
                ans += count[i] # 把數量累積
        # print(table)
        # print(count)
        return ans
