# LeetCode 1395. Count Number of Teams
# 挑3人i,j,k組隊（rating要漸增or漸減），問總共有幾種挑法
# 有1000個人要挑，三層迴圈就太慢了。可以用兩層迴圈試試
# 先決定 i,j,k 的中間 j, 再看「左邊」、「右邊」各有幾個比rank[j]小。再「排列組合」
class Solution:
    def numTeams(self, rating: List[int]) -> int:
        N = len(rating)
        ans = 0
        for j in range(1,N-1):  # 決定中間的j
            # 在 j 的左邊，有幾個比它小？ 在 j 的右邊，有幾個比它小？ 
            left_less, right_less = 0, 0
            for i in range(j):  # 巡左邊，有幾個比 rank[j] 小
                if rating[i]<rating[j]: left_less += 1
            for k in range(j+1,N):  # 巡右邊，有幾個比 rank[j] 小
                if rating[k]<rating[j]: right_less += 1
            # 全部巡完後，就知道左邊、右邊 的大小全部累積狀況
            left_greater = j - left_less  # 換算出「左邊」幾個比rank[j]大
            right_greater =  N - 1 - j - right_less   # 換算出「右邊」幾個比rank[j]大
            # 排列組合（左邊幾個 配 右邊幾個）
            ans += left_less*right_greater + left_greater*right_less
        return ans
