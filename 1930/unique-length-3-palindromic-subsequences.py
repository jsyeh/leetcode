# Subsequences 比較麻煩, 因為可以漏掉一些字母, 可能性太多, 不能用暴力法去做
# 看了 Discussion 裡, 有人提示觀察「長度為3」的特質。 這才細看題目有限定3個字母
# 所以關鍵在最左邊、最左邊, 在哪有相同的字母。只要把26個字母都巡過一次, 就行了
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        first = {} # first['a'] 代表 'a' 第1次出現的位置
        last = {} # last['a'] 代表 'a' 最後1次出現的位置
        for i, c in enumerate(s): # 字串的迴圈
            if c not in first: # 如果是新的字母
                first[c] = i # 記下第1次出現的位置
            last[c] = i # 持續更新，便知此字母最後一次出現的位置
        # 經以上迴圈，便確定每個字母第1次、最後1次出現位置
        ans = 0
        for key in first: # 如果字母有在 first出現
            if first[key]+2<=last[key]: # 距離夠遠
                inside = set() # 裡面夾的字母
                # 中間夾了幾種字母呢？ 迴圈在裡面逐個查
                for i in range(first[key]+1, last[key]):
                    if s[i] not in inside: # 若是新鮮的字母
                        ans += 1 # 就多一種答案
                        inside.add(s[i]) # 放入用過的字母
        return ans # 便能知有多少「3個字母」且「同尾相同」的答案
