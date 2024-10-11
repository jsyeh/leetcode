# LeetCode 2251. Number of Flowers in Full Bloom
# 直覺想時好像很簡單:就模擬花開的時候,再看people對應時間的花數量
# 但是花的範圍10^9很大, 不適拿用陣列模擬。
# 這題Editorial使用 sorted 的花開期，配合 heap 來讓花關掉
class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort() # 讓花照「開」的時間排序，將依序取用
        # 為了結省測試的時間，依序排好人出現的時間，依序查詢
        sorted_people = sorted(people)
        flowerN = {} # flowerN[i] 表示第i天能看到的花數

        heap = [] # heap 裡面存已開的花，且以結束時間消減
        # 所以 len(heap) 就是某個時間的花的數量

        fi = 0 # 第fi朵花開，flowsers[fi] 將會花開在 flowers[fi][0]
        # 以人出現的時間為準，依序查詢有多少花開了
        for T in sorted_people: # 某人在 T 進來看花
            while fi < len(flowers) and T>=flowers[fi][0]:
                # 還有花可以開，且 T時間之前花開的話，把花關的時間加入heap
                heappush(heap, flowers[fi][1])
                fi += 1 # 準備測下一朵花
            
            # 能開的花都開了，接下來看「花有沒有在T之前就謝了」
            while len(heap)>0 and T>heap[0]: # 花在T之前就謝了
                heappop(heap) # 花需要關閉/花謝了
            
            flowerN[T] = len(heap) # 在T時間，有flowerN[T]朵花
        
        # 全部算完後，依序算答案
        N = len(people)
        ans = [0]*N
        for i in range(N):
            T = people[i]
            ans[i] = flowerN[T]
        return ans

