# LeetCode 683. K Empty Slots
# 房間內有 n 個燈泡 1...n，一開始全關，每天開1個燈泡
# bulbs[i] = x 代表「第i+1天」會開啟「燈泡x」
# 要幾天之後，「某2個開啟的燈泡」裡面「剛好有連續k個沒開的燈泡」
# 我一開始以為用 binary search。但不行，因中間可能插入值而失敗）
# Solutions 裡 Vincent 及 LeeCGo 使用「毛毛蟲」sliding window完成，我試試看
class Solution:
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        N = len(bulbs)  # N 個燈泡
        days = [0] * N  # days[i] 對應「燈泡i」開燈的日子
        for i in range(N):
            days[bulbs[i]-1] = i+1  # 為簡化程式，都變成 0-index
        ans = inf
        left, right = 0, k+1  # 第1段，裡面有 k 個待測
        for i in range(N):
            if days[i] > days[left] and days[i] > days[right]:  # 中間還沒亮
                continue  # 很好，繼續「逐一測」中間的部分
            # 但如果中間有亮，那就不對了，要修正 left 和 right 的範圍
            if i==right:  # 運氣好，剛好 left...right 的最右邊亮，算是答案之一
                ans = min(ans, max(days[left], days[right]))  # 更新答案
            left = i  # 左邊亮的位置
            right = left + k + 1  # 中間若「空k格」後，右邊端點的位置
            if right >= N: break  # 右邊「超過陣列邊界」，結束
        if ans==inf: return -1
        return ans


        # 先把 bulbs 轉成 turnOn 陣列
        N = len(bulbs)  # N 個燈泡
        turnOn = [0] * (N+1)  # 1..N 要多1格才夠
        for i in range(N):
            turnOn[bulbs[i]] = i + 1 # 第 i + 1 天開啟的燈泡
        def helper(days):  # days 天後，是否「剛好k個沒開的燈泡」夾在2個開啟的燈泡中間
            lastOn = -1. # 前一個亮的「在哪一個」
            for i in range(1, N+1):
                if turnOn[i]<=days:  # 這天之前有開
                    if lastOn != -1 and i-lastOn == k:
                        return True
                    lastOn = i
            return False
        ans = bisect_left(range(1,N+1), True, key=helper)
        if ans==1: return -1
        return ans
