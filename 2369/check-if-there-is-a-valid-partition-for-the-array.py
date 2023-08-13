# 1. subarray/substring 都要連續。subsequence不用連續
# 2. 像玩牌，要拆出2相同、3相同、3連續。要剛好、要全拆
# 真的DFS去做可能會很慢。可先巡過，不可能就提早False
# 偷看 Editorial 有講到 Dynamic Programming 有道理，開始試
class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        table = [False]*(N+1)
        # table[i]  i 個字，結束在 nums[i+1] 是否OK

        table[0] = True # 最基礎：切齊最前面
        if nums[0]==nums[1]: # 2個字母相同的狀況
            table[2] = True # 補齊第2個基礎
        # 前面將「終止條件」設定好
        for i in range(3,N+1): # 後面迴圈就簡單了
            if nums[i-1]==nums[i-2] and table[i-2]:
                table[i] = True
            if nums[i-1]==nums[i-2] and nums[i-2]==nums[i-3] and table[i-3]:
                table[i] = True
            if nums[i-1]==nums[i-2]+1 and nums[i-2]==nums[i-3]+1 and table[i-3]:
                table[i] = True
        # print(table)
        return table[N]
