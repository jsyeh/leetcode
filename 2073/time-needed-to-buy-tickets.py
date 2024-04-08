# 想知道第k個人 要等多久才能買完票
# 要等他前面「<=它」的票數, 還有它後面「<=它-1」的票數
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        for i in range(k+1):
            ans += tickets[i] if tickets[i]<tickets[k] else tickets[k]
        for i in range(k+1,len(tickets)):
            ans += tickets[i] if tickets[i]<tickets[k]-1 else tickets[k]-1
        return ans
