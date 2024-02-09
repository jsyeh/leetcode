# 這題我之前有寫過，但我已看不懂那時的寫法。今天的挑戰題又出現一次。
# 在 Discussion 裡，meanup 建議「先解 300. Longest Increasing Subsequence」
# 我回去看 LeetCode 300 LIS 那題，果然發現 「遞增」與「倍數關係」很像
# 所以就照著這個原則寫，配合 mstuebs 給的測資，印出 max(tables) 對應是對的
# 這時再利用 table.index(max(table)) 找到 i 後，prev[i] 往回逐項找，就成功了
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort() # 從小到大排好
        N = len(nums)
        table = [1]*N # 裡面會存 table[i] 表示「排序後的第i數」結尾的最長group大小
        table[0] = 1 # 只有1個答案，就是自己本身
        prev = [-1]*N # 找到 i 的前一項，prev[i]=-1表示沒有前一項
        for i in range(1,N): # 想更新 table[i]
            for p in range(i): # 前面的項
                # 如果是倍數，且可接成更長的 group 時
                if nums[i]%nums[p]==0 and table[p]+1>table[i]:
                    table[i] = table[p] + 1 # 更新 table
                    prev[i] = p # 指到前一項的位置
        # print(max(table)) 檢查後，確定正確。接下來要裝 ans list 建出來
        ansI = table.index(max(table)) # 找到 table[i] 最大值 對應的 i
        ans = []
        while ansI != -1: # 只要還能回溯追蹤
            ans.append(nums[ansI]) # 就把數字加入
            ansI = prev[ansI] # 並持續（往前）追蹤
        #print(table)
        #print(prev)
        return ans
# case 44/49: [2,3,8,9,27]
