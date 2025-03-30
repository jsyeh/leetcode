# LeetCode 763. Partition Labels
# 每種字母只能出現在某一段 part，不能跨越 part，問最多能分幾 parts
# 看起來像 meeting 時間 merge interval 的問題，每種字母「開始、結束」能切幾段
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        left, right = {}, {}  # 用來放字母的第一次出現位置、最後一次出現位置
        for i,c in enumerate(s):
            if c not in left:  # 字母沒出現過
                left[c] = right[c] = i  # 記錄位置「左界」同時也是「右界」
            else:  # 若有出現過
                right[c] = i  # 繼續更新「右界」
        pos = []  # 能斷開的位置
        p0, p1 = -1, -1  # 前一筆的位置
        for a, b in zip(left.values(), right.values()):  # 剛好 left 已是小到大排好，開始 merge
            if p1 < a:  # 前一筆 與 現在這筆 分開
                pos.append(a)  # 記下「能分割」的位置
                p0, p1 = a, b  
            else:  # 無法分割
                p1 = max(p1, b)  # 就「合併兩筆」，更新「右界」
        ans = [pos[i+1] - pos[i] for i in range(len(pos)-1)]  # 將「分割位置」兩兩相減，變成「長度」
        ans.append(len(s)-pos[-1])  # 最後一筆的長度
        return ans  # 就算出每一筆的長度了
