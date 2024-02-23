# 給許多「飛機航班」（from,to,price)，限定「轉機k次」（中間停的城市）以內
# 問「最便宜」的機票多少錢。
# 這題好難，我錯了好多次。我是用 priority queue 來把「便宜」的各種走法試過
# 價格「足夠」到達目的地，就結束。若走不到or超過步數，就return -1
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # 要建個資料結構，了解「某城市」到其他城市的對照表
        fromTo = defaultdict(list)
        for s,d,p in flights: # src/from, dst/to, price
            fromTo[s].append((d,p)) # 記錄 dest 及 price
        cheapest = [[inf]*(k+1) for _ in range(n)] # cheapest[i][k] 表示「從src到i的最便宜機票的價格」
        # 經過k stops。有可能「轉機」越多，會有「更低的價錢」
        heap = [] # 要利用 price 排序的 priority queue
        heappush(heap, (0,0,src)) # (price累積費用, stops中停的站數, city到達哪個城市)

        while len(heap)>0:
            price, stops, city = heappop(heap) # 現在最便宜的票價，可src到city,中轉城市 stops個
            if city == dst: return price # 到達目的地，就是最便宜的走法
            if stops>k: continue # 超過轉機次數，就避開這筆資料

            for d,p in fromTo[city]: # 下一個目的地
                if cheapest[d][stops] > price + p: # 同樣條件但更便宜
                    cheapest[d][stops] = price + p # 就更新
                    heappush(heap, (cheapest[d][stops],stops+1,d)) # 並丟進heap再試
                    #print(city,d,p,cheapest)
        #print(fromTo)
        #print(cheapest)
        return -1 # 無法走到
# case 18/53: n=5, flights=[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], src=2, dst=1, k=1
# case 43/53: n=4, flights=[[0,1,1],[0,2,5],[1,2,1],[2,3,1]], src=0, dst=3, k=1
# case 46/53: n=5, flights=[[0,1,5],[1,2,5],[0,3,2],[3,1,2],[1,4,1],[4,2,1]], src=0, dst=2, k=2
# case 3/53: n=5, flights=[[4,1,1],[1,2,3],[0,3,2],[0,4,10],[3,1,1],[1,4,3]], src=2, dst=1, k=1
# case 47/53: n=13, flights=[[11,12,74],[1,8,91],[4,6,13],[7,6,39],[5,12,8],[0,12,54],[8,4,32],[0,11,4],[4,0,91],[11,7,64],[6,3,88],[8,5,80],[11,10,91],[10,0,60],[8,7,92],[12,6,78],[6,2,8],[4,3,54],[3,11,76],[3,12,23],[11,6,79],[6,12,36],[2,11,100],[2,5,49],[7,0,17],[5,8,95],[3,9,98],[8,10,61],[2,12,38],[5,7,58],[9,4,37],[8,6,79],[9,0,1],[2,3,12],[7,10,7],[12,10,52],[7,2,68],[12,2,100],[6,9,53],[7,4,90],[0,5,43],[11,2,52],[11,8,50],[12,4,38],[7,9,94],[2,7,38],[3,7,88],[9,12,20],[12,0,26],[10,5,38],[12,8,50],[0,2,77],[11,0,13],[9,10,76],[2,6,67],[5,6,34],[9,7,62],[5,3,67]], src=10, dst=1, k=10
# 好慘，TLE超時。我決定學習 Artificial_Life 的方法，加個 visited 來加避開
# 也就是照舊，把我的 cheapest[d][stops] 拿來用
