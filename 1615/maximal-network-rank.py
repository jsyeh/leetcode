# road rank定義：road兩頭城市a,b，有碰到的road總數 但(a,b)只能算1次
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        # 用笨方法試試：先建出「每個城市相鄰的城市」，a,b相接的話再扣掉1
        table = set() # 用來查表，確任 a,b城市有無相接
        neighbor = [0]*n
        for [a,b] in roads: # 每條路兩端的城市 a, b
            neighbor[a] += 1 # 多1條路相接
            neighbor[b] += 1 # 多1條路相接
            table.add(a*100+b) # 有100個城市
            table.add(b*100+a) # 利用公式，可快速查2城市有無相接
        
        print(neighbor)
        ans = 0 # 準備找 max road rank 
        #for [a,b] in roads: # 每一條路的 a,b 兩城市
        for a in range(n):
            for b in range(n):
                if a==b: continue
                temp = neighbor[a] + neighbor[b] # 把它們的 neighbors 交集
                print(a, b, temp)
                if (a*100+b) in table: temp -= 1 # 直接相鄰，會多算1次，要扣掉
                print(temp)
                if temp>ans: ans = temp # 若更大，更新
        return ans
# case 13/83: 2 [[1,0]] 2個城市，互連，它們的 road rank 是2還是1？
# If a road is directly connected to both cities, it is only counted once.

