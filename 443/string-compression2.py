# LeetCode 443. String Compression
# 字串壓縮時，長度1的字母「不用加數字」，其他要加數字。
# 將「壓縮後的字串」逐一放回 chars 並回傳「壓縮後」字串長度
class Solution:
    def compress(self, chars: List[str]) -> int:
        groupsC = []  # 某一個字母
        groupsN = []  # 連續出現幾次
        prev = -1  # 前一個字母
        for c in chars:
            if c != prev:  # 若與前一個字不「不同」
                prev = c  # 更新
                groupsC.append(c)  # 塞入陣列
                groupsN.append(1)  # 從1開始數
            else: groupsN[-1] += 1  # 重覆時，+1
        ansN = 0  # 開始累積、更新 chars 字串的內容
        for c, n in zip(groupsC, groupsN):  # 依序取出
            chars[ansN] = c  # 先塞入字母
            ansN += 1
            if n==1: continue  # 若只有1個字母，就不要加數字
            for c in str(n):  # 2個字母以上，要加數字（對應的字串）
                chars[ansN] = c  # 再塞入「數字」對應的字母
                ansN += 1
        return ansN
