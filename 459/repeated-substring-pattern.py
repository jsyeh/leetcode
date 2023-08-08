# 這題的題目其實有點難，所以我之前有偷看過解答再寫
# 原則是：如s是由許多小成份重覆組成的話，那兩個字s+s接起來，也一定是重覆
# 更巧的是，如果頭尾更減掉一個字母，因為有重覆的部分在中間，所以還是找得到 s 在裡面
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        s2 = s+s
        s2 = s2[1:len(s2)-1]
        # print(s2)
        if s in s2: return True
        else: return False
