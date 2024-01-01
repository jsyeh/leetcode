# 每個小孩 greed[i] 想要的大小不同，你手上 cookie[i] 的大小也不同
# 每個小孩最多給 one cookie，你可以滿足幾個小孩？
# 感覺只要都 sort 好，再逐一查看能不能滿足即可
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort() # 小孩 greed 貪心的程度
        s.sort() # 手上 cookie 的 size
        gN, sN = len(g), len(s)
        i, j = 0, 0
        ans = 0
        while i<gN and j<sN: # 還沒走到最後
            if g[i]<=s[j]: # 只要還給得起
                ans += 1 # 就給餅乾
                i, j = i+1, j+1 # 並更新 index
            else: # 如果給不起，一定是餅乾不夠大
                j += 1 # 就換更大的餅乾
        return ans
