# 這題目看似複雜，其實有個神奇的特質：XOR運算，可以反過來
# 也就是 A ^ B 得到 C 的話，  A ^ C 會得回原本的 B
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        for i in range(N-1,0,-1): # 用倒過來的迴圈，避免蓋到值
            pref[i] = pref[i] ^ pref[i-1] # 相鄰項可推出
        return pref
