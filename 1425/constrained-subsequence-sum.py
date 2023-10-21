# 這個方法，有偷偷參考 Editorial 的 Prioirty Heap 的解法
# 有個 heap 會記錄之前全部每一格的最佳的值，而且最好的最佳值會在 heap[0] 裡
# 但是因為距離 k 的條件，所以會有個 while迴圈，把距離太遠的都丟掉
class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        ans = nums[0]
        heap = [(-nums[0], 0)] # 先把第0個先拿進Heap做記錄

        for i in range(1, len(nums)): # 接下來處理第1個之後的值
            while i - heap[0][1] > k: # heap的最佳值，距離太遠了
                heappop(heap) # 丟掉、不考慮
            # 所以離開while迴圈時 heap[0]是距離夠近的最好的
            curr =  -heap[0][0] + nums[i] # 要考慮第 i 格要用它時，最好的值是多少
            if -heap[0][0]<0: # 之前最佳值竟然是負的
                curr = nums[i] # 不要用之前的任何值，直接自立門戶
            if curr > ans: # 現在的值如果更好
                ans = curr # 就更新ans
            heappush(heap, (-curr, i) ) # 把第i格對應的最佳值，加入heap
        return ans

