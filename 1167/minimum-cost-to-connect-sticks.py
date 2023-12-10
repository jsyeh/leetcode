# 直覺的想法，是每次「排最短」的兩根stick接起來
class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapify(sticks) # 先變成 heap 方便找到最短的stick
        ans = 0
        while len(sticks)>1: # 只要還有2個以上的sticks
            a = heappop(sticks) # 就先挑最小根
            b = heappop(sticks) # 再挑出次小根
            ans += a+b # 耗費的 cost
            heappush(sticks, a+b) # 合成後的新stick加回去
        return ans

