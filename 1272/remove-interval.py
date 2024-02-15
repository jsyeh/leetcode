# 原本的 intervals 去除 toBeRemoved 區段，剩下的 return 
class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for interval in intervals: # 把全部的可能性都裁過1次
            if interval[1] <= toBeRemoved[0]: 
				ans.append(interval)
            elif interval[0] >= toBeRemoved[1]: 
				ans.append(interval) # 這裡有機會加速：離開迴圈，後面全加入
            elif interval[0] < toBeRemoved[0] and interval[1] > toBeRemoved[1]:
                ans.append([interval[0],toBeRemoved[0]])
                ans.append([toBeRemoved[1],interval[1]])
            elif interval[0] < toBeRemoved[0] and interval[1]<= toBeRemoved[1]:
                ans.append([interval[0],toBeRemoved[0]])
            elif interval[0] <= toBeRemoved[1] and interval[1] > toBeRemoved[1]:
                ans.append([toBeRemoved[1],interval[1]])
        return ans
