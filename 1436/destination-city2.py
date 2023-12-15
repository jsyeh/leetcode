# LeetCode 1436. Destination City
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        notAns = set()
        
        for a,b in paths: # 先巡第1輪, 先檢查a
            notAns.add(a) #出發點,不是答案
        
        for a,b in paths: # 第2輪, 再檢查b
            if b not in notAns: # b不在出發裡,就是答案
                return b # b 不是「不是答案」
