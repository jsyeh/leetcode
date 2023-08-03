# 嚴格遞增數列，而且是 subsequence 也就是可挑
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        ans = 1
        N = len(nums)
        table = [0]*N # table[i] 包含 nums[i] 的 LIS 長度
        table[0] = 1 # nums[0] 本身單獨就是LIS，長度為1 。
        # 上面這行可不寫，只要下面的 for迴圈 range(N) 即可
        for i in range(1,N):
            table[i] = 1 # nums[i] 本身單獨就是LIS，長度為1 。
            for k in range(i): # nums[i] 左邊的數
                # 數字左小、右大，而且 LIS 的值有更好的話
                if nums[k]<nums[i] and table[k]+1>table[i]:
                    table[i] = table[k] + 1 # 就更新 LIS 的值
            if table[i] > ans:
                ans = table[i]
        # print(table)
        # return table[N-1] 答案不是最後一筆
        return ans

# case 34/54: [1,3,6,7,9,4,10,5,6] 答案不是最後一筆，不能看 table[N-1]
# case 53/54: [0] 答案預設要是 1 因為只要有數字，LIS至少就有1 (不能寫 ans = 0)
