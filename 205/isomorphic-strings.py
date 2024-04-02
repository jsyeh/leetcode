# 同構體，也就是「逐字結構相同」只是換字母而已
# (1) 字母出現頻率（分布狀況）相同，且(2) 一對一對應
# 註：稍早分析錯誤, 「誤以為」是字母出現的頻率(分布狀況)是否相同
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        N1, N2 = len(s), len(t)
        if N1 != N2: return False # 長度不同，一定錯

        table1 = collections.defaultdict(str) # s 對應到 t 的對照表
        table2 = collections.defaultdict(str) # t 對應到 s 的對照表
        for i in range(N1):
            if s[i] not in table1 and t[i] not in table2:
                table1[s[i]]=t[i] # 沒對照過，可建立對照表
                table2[t[i]]=s[i]
            elif table1[s[i]] != t[i] or table2[t[i]] != s[i]:
                return False # 本次對應 與之前不同，就錯了
        return True
# case 6/45: "badc" vs. "baba"
