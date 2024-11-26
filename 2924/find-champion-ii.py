# LeetCode 2924. Find Champion II
# 有 n 隊，edges 有對戰成績（a勝b），請找出冠軍。
# 冠軍「不敗」沒有輸任何一隊。「只能有一隊」是冠軍，不然就 return -1
class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        win = [0]*n  # 記錄每隊「勝幾場」
        lost = [0]*n  # 記錄每隊「輸幾場」
        for a, b in edges:  # a勝b
            win[a] += 1
            lost[b] += 1
        winner = -1  # 找不到冠軍的話，return -1
        winnerN = 0  # 數一數，有幾隊「不敗」
        for i in range(n):
            if lost[i]==0:  # 找到「不敗」的隊伍
                winner = i
                winnerN += 1
        if winnerN == 1: return winner  # 只有1隊「不敗」，很好！
        else: return -1

