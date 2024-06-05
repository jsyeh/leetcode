# 車牌有「英文、數字」，要重新排版，讓每段有k個字母。
class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        plate = []  # 車牌裡有有效「英數字」
        for c in s:  # 逐字分析車牌符號
            if c.isalpha():  # 遇到字母
                plate.append(c.upper())  # 就變成大寫，記錄下來
            elif c.isdigit():  # 遇到數字
                plate.append(c)  # 也記錄下來
        N = len(plate)  # 目前有效的英數字有幾個
        ans = []  # 用來「分段存」車牌裡「每一段長度為k」的字串
        if N%k>0:  # 不整除的話，要先記下最前面那段
            ans.append(''.join(plate[:N%k]))
        for i in range(N%k, N, k):  # 分段切
            ans.append(''.join(plate[i:i+k]))  # 每段長度為k
        return '-'.join(ans)  # 再全部結合起來

