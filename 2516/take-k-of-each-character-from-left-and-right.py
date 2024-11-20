# LeetCode 2516. Take K of Each Character From Left and Right
# a,b,c三種字母都要收集到k個以上。問你最少要左右兩端拿幾個字母，才能成功
# 這題看起來，是「反過來」的毛毛蟲的題目。
class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        if k==0: return 0  # 什麼都不用，那就0個即可
        counter = Counter(s)  # 全部字母都用上
        if counter['a']<k or counter['b']<k or counter['c']<k:
            return -1  # 全部字母都用上後，竟然還不夠，就失敗
        N = len(s)
        ans = left = 0
        for right in range(N):  # 「反過來」的毛毛蟲，是要扣掉的
            counter[s[right]] -= 1  # 吃掉（不用）
            while counter[s[right]]<k:  # 糟，不夠用
                counter[s[left]] += 1  # 吐回去（要用）
                left += 1
            if counter['a']>=k and counter['b']>=k and counter['c']>=k:
                ans = max(ans, right-left+1)
        return N - ans  # 倒過來想
