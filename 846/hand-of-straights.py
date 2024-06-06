# LeetCode 846. Hand of Straights
# 在玩牌時, 如果有「同花順」會很厲害。這種「把數字小到大連續」的牌, 想用電腦組出來
# 這個straights「順子」的要求的張數, 由題目 groupSize 來決定。
# 能不能「滿手都是 straights」呢? 
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        hand.sort()  # 先從小到大排好
        counter = Counter(hand)  # 再統計每個數字的出現次數
        for c in counter:  # 希望這時候的 c 是從小到大依序出現(應該吧)
            now = counter[c]  # 順子開頭的數量
            if now==0: continue  # 避開「數量是0個」的狀況 
            for i in range(c, c + groupSize):  # 順子開頭的數字c開始, 連續 groupSize 個
                counter[i] -= now  # 照這個數量, 都扣減到它
                if counter[i]<0: return False  # 不夠扣減, 那就 GG 失敗了
        return True  # 恭喜你, 沒有失敗, 就成功了
