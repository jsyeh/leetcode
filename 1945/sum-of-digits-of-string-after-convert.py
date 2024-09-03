# LeetCode 1945. Sum of Digits of String After Convert
# 字母 a-z 轉成數字 1-26，再把「每個位數」的數字「加起來」，做k次
class Solution:
    def getLucky(self, s: str, k: int) -> int:
        ans = []
        for c in s:  # 先將字母，變成1-26的數字（對應的字串）
            ans.append(str(1+ord(c)-ord('a')))
        s = ''.join(ans)  # 把字串的 list 結合成長字串
        for i in range(k):  # k次轉換
            total = 0  # 放「加總」的結果
            for c in s:  # 將字串s的字母「拆解」成字母，轉成數字，再加起來。
                total += int(c)  # 逐一加進去
            s = str(total)  # 再把數字，變回字串，方便「下一輪」再拆解
        return int(s) # 把字串，轉成整數，再回傳
