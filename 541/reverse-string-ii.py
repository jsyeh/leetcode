# 有個奇怪的「反轉」的規則：k個反轉、k個不反轉，持續下去
# 如果最後「不夠k個的話」把那些全反轉
# 如果最後「不夠k個不反轉」的話，那些就不反轉
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        ans = []  # 因字串越接越長、太慢，用list較快
        k2 = 0  # 每段「反轉」的開始位置
        N = len(s)
        ans.append( s[k2+k-1::-1] )  # 最前面一段的反轉
        # print( s[k2+k-1::-1] )  # 印出來，方便debug
        k2 += k
        while k2 < N:
            ans.append( s[k2:k2+k] )  # 不反轉
            # print( s[k2:k2+k] )  # 印出來，方便debug
            k2 += k
            ans.append( s[k2+k-1:k2-1:-1] )  # 又反轉
            # print( s[k2+k-1:k2-1:-1] )  # 印出來，方便debug
            k2 += k
        return ''.join(ans)  # 把list再接回字串
