# nums[i][0]...nums[i][1] 是車子佔的範圍
# 問總共佔了多少個座標點。因為數字很小，暴力迴圈陣列，即可解決。
class Solution:
    def numberOfPoints(self, nums: List[List[int]]) -> int:
        points = [0]*101 # 一開始座標點「都沒人佔著」
        for start,end in nums: # 照著 input 逐段更新
            for i in range(start, end+1): # 每個範圍內的點
                points[i] += 1 # 都增加1個人佔用
        ans = 0
        for i in range(101): # 再次針對每個點檢查
            if points[i]>0: ans += 1 # 如果有人佔用，+1
        return ans # 便可知道總共有多少座標點被佔用
