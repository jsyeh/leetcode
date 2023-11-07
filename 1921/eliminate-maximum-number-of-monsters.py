# 怪物入侵，你知道他們一開始的位置、每分鐘移動的距離
# 你每分鐘只能解決1隻怪物，怪物的碰到你時，馬上結束
# 問你能解決幾隻怪物
# 資料有10^5筆，數值1...10^5，所以不能用暴力法模擬
# 啊！可以算出「怪物抵達的時間」，再用時間來排序，看能解決幾隻

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        N = len(dist)
        arriveT = [dist[i]/speed[i] for i in range(N)]
        # 算出抵達的時間, 會是 float 浮點數
        arriveT.sort() # 再從小到大排好
        
        # print(arriveT)
        # 在T=0時，可以有第1擊
        for i in range(N):
            if arriveT[i]<=i: # 如果怪物已到，就來不及解決它
                return i
        return N # 全部檢查都沒問題的話，可以解決全部N隻怪物
