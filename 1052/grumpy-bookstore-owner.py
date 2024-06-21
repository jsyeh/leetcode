# LeetCode 1052. Grumpy Bookstore Owner
# 愛生氣的書店老板, 如果 grumpy[i] 是1的話, 就會對「顧客」生氣。還好, 老板能忍住「連續幾分鐘」不生氣
# 但何時「忍住不生氣」呢? 就交給你來計算。總之「只能忍住幾分鐘」, 最多能有幾位顧客被「好好對待」?
# 可使用 sliding window, 想像「不生氣的時間」就像「一條毛毛蟲」尾在左、頭在右, 慢慢往右「邊爬邊更新」
class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        N = len(customers) # 總共有N個時間單位要處理
        ans = 0
        for i in range(minutes): # 先假設「最一開始的時段」是不生氣的
            ans += customers[i] # 能服務這段時間這些客人
        for i in range(minutes, N):  # 後面的時段, 則照著老板的心情, 看還能服務多少客人
            if grumpy[i]==0:  # 如果這個時段沒有生氣
                ans += customers[i]  # 就可好好服務客人
        
        # 接下來 sliding window 毛毛蟲要登場了(「忍住不生氣」的時段「往右滑動」)
        now = ans  # now 對應「滑動」過程中, 能好好對待的總顧客人數
        j = 0 # i 是頭、j是尾
        for i in range(minutes, N):  # 接下來, 像毛毛蟲一樣, 往右滑動
            if grumpy[i]==1: now += customers[i]  # 右邊「忍住」能多服務的客人
            if grumpy[j]==1: now -= customers[j]  # 左邊「不忍了」而少服務的客人
            ans = max(ans, now)  # 持續更新答案
            j += 1  # 迴圈的頭i往右移時, 尾j也往右移
        return ans
