# 每天 temperatures[i] 的值不同，想知道「幾天後」會變熱
# ans[i] 就是「第i天」往右數，「幾天後」變熱。
# 因為 10^5 很多天，不能用暴力法。Mono stack 應可解，但我不太熟。
# Editorial 的解法：從左往右巡，每天i都加入「待處理」stack中，對應的溫度是單調漸增/漸減的。
# 如果「stack裡prev之前」的溫度<今天t，就更新 ans[prev]（因為今天比較熱嘛）while持續更新
# 直到「天啊，之前天氣太熱，今天i不夠熱、搞不定」就「留在stack」不要取出，再把今天i「加入stack」
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        N = len(temperatures) # 有幾天要處理
        ans = [0] * N
        stack = []
        for i, t in enumerate(temperatures): # 第i天的溫度 t = temperatures[i]
            # 若有「待處理」的stack，且它最後一筆stack[-1]對應的溫度<今天的溫度t
            while len(stack)>0 and temperatures[stack[-1]] < t:
                prev = stack.pop() # 今天的溫度t，可以溫暖幾天前的天氣吧？ 更新
                ans[prev] = i - prev # 今天天氣比「之前」熱，可更新ans[之前] 的值
            stack.append(i) # 今天也加入「待處理」stack裡
        return ans
