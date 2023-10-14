# 本來沒有頭緒，參考Editorial的方法1，好像有點道理。所以試看看
class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        N = len(cost) # 有幾個要考慮的 index
        @cache
        def helper(index, remain)->int: # 要花多少錢
            if remain<=0: # 全部走完
                return 0 # 沒事，最後0個牆不用錢
            if index==N: # 沒辦法順利走完
                return inf
            # 如果現在 index 對應的牆要花錢請人漆油漆
            paint = cost[index] + helper(index+1, remain-1-time[index]) 
            # 它要花費 time[index]的時間，能免費漆time[index]個牆
            # 所以剩下的牆是 remain - 1 - time[index]

            # 如果現在 index 對應的牆不要花錢請人漆油漆，再往後問
            dontpaint = helper(index+1, remain)
            return min(paint, dontpaint)
            
        return helper(0, N)
