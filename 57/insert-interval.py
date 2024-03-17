# 一堆(不overlap的) intervals 照 start 排序好
# newInterval 要插入
# 要求「保持」照start排好，且「不能overlap」，也需要merge
# 去年在寫時，我寫得很複雜、嘗試失敗 10次，只成功1次
# 這次發現 intervals vs. s2,e2 的3種狀況「都在前」「都在後」「交錯」
# 再看 StefanPochmann 的 Solution 2 想法是類似的，就寫吧
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        s2, e2 = newInterval # 要插入的 start, end 時間
        left, middle, right = [], [], []
        # 要處理的狀況有幾種：s2,e2都在前面、交錯、都在後面
        for start, end in intervals:
            if end<s2: # 在之前
                left.append([start,end]) # 「左邊國」
            elif e2<start: # 在之後
                right.append([start,end]) # 「右邊國」
            else: # 最難處理的交錯，就是要合併，將s2,e2放大
                s2 = min(start,s2) # 合併的新起點（偏左）
                e2 = max(end,e2) # 合併的新終點
        middle.append([s2,e2]) # 「中間國」
        return left + middle + right # 「三國」接起來
