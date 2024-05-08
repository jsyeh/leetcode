# LeetCode 506. Relative Ranks
# 相對排名：分數高到低，分別是Gold Medal, Silver Medal, Bronze Medal,
# 再來就 4,5,6...下去。我的想法，是先把 index i 和 score 合在一起
# 以 score從大到小排，答案再依序放入
class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        N = len(score)  # 先了解有幾位選手
        table = [(score[i], i) for i in range(N)]  # 表格：分數及index
        table.sort(reverse=True)  # 照著score[i]的分數排序，從大到小。
        # 在排序時，對應的index也跟著一起動
        ans = [0] * N  # 用來放答案的 ans，將會放對應的字串，從 '1' 開始
        for rank, (s, i) in enumerate(table):
            ans[i] = str(rank + 1)  # 對應的字串，從 '1' 開始
            if ans[i] == '1':  # 如果是第1名，改成英文的「金牌」
                ans[i] = 'Gold Medal'
            elif ans[i] == '2':  # 如果是第2名，改成英文的「銀牌」
                ans[i] = 'Silver Medal'
            elif ans[i] == '3':  # 如果是第3名，改成英文的「銅牌」
                ans[i] = 'Bronze Medal'
        return ans
