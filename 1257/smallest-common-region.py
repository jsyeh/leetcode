# LeetCode 1257. Smallest Common Region
# 一堆 regions，其中 regions[i][0] 包含「右邊全部」的 regions[i][k]
# 給 region1 和 region2，找出他們共同的地理區域範圍
# 可由 regions 建出 tree 結構，再由兩個 nodes 分別「往上」找出「共同的root」 
class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        parent = defaultdict(str) # 每區「往上」有1個parent
        for region in regions:
            for i in range(1,len(region)): # 對右邊每一個
                parent[region[i]] = region[0] # 建立「往上」關係
        # 先由 region1 「往上」建立「在哪裡」的關係
        where1 = set() # region1 在哪裡，
        while region1 != '':  # 最後會到沒東西的空字串
            where1.add(region1)  # 加入 where1
            region1 = parent[region1] # 往上一層
        # 再由 region2 「往上」查，找到 where1 就是答案
        while region2 != '':
            if region2 in where1:  # 有共通，就是答案
                return region2
            region2 = parent[region2] # 沒共通時，繼續往上
        return '' # 寫好玩的（程式不會走到這行，因為題目「保證」會有「共同」的答案）
