# 調整後的字串，「數字、字母」要交錯
# 可先收集字母（分類），再逐建出來
class Solution:
    def reformat(self, s: str) -> str:
        a, a2 = [], [] # 用來放字母、數字
        for c in s:
            if c.isdigit(): a2.append(c) # 數字放一堆
            else: a.append(c) # 字母放一堆
        if len(a)<len(a2): 
            a, a2 = a2, a # 讓長的放在 a，短的放在 a2
        if len(a)>len(a2)+1: return '' # 數目差太多，失敗

        ans = []
        while len(a)>0 and len(a2)>0: # 兩個都還能一起吐
            ans.append(a.pop()) # 吐給 ans
            ans.append(a2.pop()) # 吐給 ans
        if a: ans.append(a.pop()) # 還有多的話，再吐
        return ''.join(ans) # 合成字串
