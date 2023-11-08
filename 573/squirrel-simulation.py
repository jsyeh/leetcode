# 小松鼠，把nuts放到 tree 的位置。5000個nuts、只有一棵樹。
# 第一顆nut的距離，是小松鼠to松果to樹，後面的距離都是固定的松果to樹
# 所以可簡化成：全部松果到樹的距離*2，但有一個距離要被松鼠to松果距離取代
class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:
        N = len(nuts)
        saveDist = -inf # 裡面會存「節省的距離」
        # 也就是「松鼠to松果 vs. 樹to松果，節省幾步」
        # 排序後，便知道省最多步的走法，去更新ans
        ans = 0
        for i in range(N):
            r, c = nuts[i]
            tree2nut = abs(tree[0]-r)+abs(tree[1]-c)
            ans += tree2nut
            temp = tree2nut - abs(squirrel[0]-r) - abs(squirrel[1]-c)
            if temp>saveDist: saveDist = temp

        return ans*2 - saveDist
        
