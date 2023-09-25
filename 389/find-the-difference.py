class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        H1 = {} # Histogram of s 每個字母出現次數
        for c in s: # 統計 s 裡每個字母出現的次數
            if c in H1:
                H1[c] += 1
            else:
                H1[c] = 1
        # 接下來，反過來扣掉。
        for c in t:
            if c in H1 and H1[c]>0:
                H1[c] -= 1 # 如果能扣掉t出現的字母，就扣掉
            else: # 不能扣掉的話，
                return c # 這個字母就是多出來的字母

