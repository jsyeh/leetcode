# 題目想知道「如果中毒持續duration」那在連續攻擊的 timeSeries 時，總共中毒多久
# 所以如果攻擊時還在中毒的話，那 ans 只會再增加 t + duration - lastT 的時間
# 如果攻擊時沒有中毒，那 ans 會增加 duration
class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        ans = 0
        lastT = 0
        for t in timeSeries:
            if lastT>t: # 現在還在中毒中，時間不用加滿，只要加「增加」的部分
                ans += t + duration - lastT
            else: # 現在沒中毒，時間要加滿
                ans += duration
            lastT = t + duration
        return ans
