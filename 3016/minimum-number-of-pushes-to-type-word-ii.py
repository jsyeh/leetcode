# LeetCode 3016. Minimum Number of Pushes to Type Word II
# 電話數字鍵裡，有附英文字母：2有a,b,c三字母：按1次a、2次b、3次c。
# 現在想根據頻率，重新調整數字鍵上的英文，讓「按出 word 所需次數最少」
class Solution:
    def minimumPushes(self, word: str) -> int:
        counter = Counter(word) # 先統計
        freq = list(counter.values()) # 再把「出現次數」取出來
        freq.sort(reverse=True) # 「出現次數」照「多到少」排序
        # greedy法：照著字母出現次數，放到（2到9）共8鍵放好。
        ans = 0
        for i, times in enumerate(freq):
            ans += times * (i//8 + 1) # i//8+1 對應「要重覆按的次數」
        return ans
