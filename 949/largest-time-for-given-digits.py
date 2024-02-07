# 其實4個數字，排列組合，總共才4*3*2*1 共24種而已
# 所以「全部測一次」即可
# 使用 Editorial 介紹的 itertools.permutations()
class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        arr.sort(reverse=True) # 由大到小排
        for h1,h2,m1,m2 in itertools.permutations(arr):
            hh = h1*10 + h2
            if hh>23: continue
            mm = m1*10 + m2
            if mm>59: continue
            return f'{hh:02}:{mm:02}'
        return '' # 找不到答案
