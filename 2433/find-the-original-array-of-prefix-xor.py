# 這題目看似複雜，其實有個神奇的特質：XOR運算，可以反過來
# 也就是 A ^ B 得到 C 的話，  A ^ C 會得回原本的 B
class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        N = len(pref)
        ans = [0]*N

        ans[0] = pref[0]
        p = ans[0] # 前一項XOR累積的值
        for i in range(1,N):
            ans[i] = p ^ pref[i] # 繼續算
            p = pref[i] # 換新的 p，也就是 XOR 累積的結果
        
        return ans
