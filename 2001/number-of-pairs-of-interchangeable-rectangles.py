# 相似長方形：長寬比一樣。問有幾組pairs 的相似長方形
# 可利用 gcd(a,b) 來約分，再丟到 hashmap 以便看有無重覆
class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio = defaultdict(int) # 某比例，有幾組重覆
        def gcd(a,b)->int: # 最大公因數
            if b==0: return a
            return gcd(b,a%b)
        # 因擔心 float 精確度，所以用「最大公因數」約分
        # 但有人直接用 float 當成 key 好像也可以正確

        for a,b in rectangles: # 記錄長寬比
            g = gcd(a,b) # gcd
            r = str(a//g)+' '+str(b//g) # ratio
            ratio[r] += 1
        ans = 0
        for r in ratio: # 梯形公式 1+...+(r-1)
            ans += (ratio[r]-1)*ratio[r]//2
        return ans
