# s 比較長, p 比較短, p重新組合的anagram, 出現在 s 的哪些開始地方
# 使用 running window 逐一測試即可
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sN, pN = len(s), len(p) # 對應的長度
        if sN < pN: return [] # s長度不夠, 沒辧法組出 anagram

        pH = Counter(p) # 用來統計p的字母出現次數
        sH = Counter(s[:pN]) # 用來統計s的前pN個數字
        ans = []
        print(pH-sH)
        if len(pH-sH)==0: ans.append(0) # 第0個比較
        for i in range(sN-pN): # 長度差,便是迴圈要做的事
            sH[s[i]] -= 1
            sH[s[i+pN]] += 1
            if len(pH-sH)==0: ans.append(i+1)
        return ans
            
