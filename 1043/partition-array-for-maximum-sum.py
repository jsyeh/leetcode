# 把 arr 切很多段，每一段最多k個數。找出每段的「最大值」，每個數都變成「最大值」
# ex. 1, 15, 7, 9, 2, 5, 10
#     ^^^^^^^^  ^  ^^^^^^^^
#     15,15,15, 9, 10,10,10 加起來最大
# 剛看，沒什麼頭緒，以為是 mono stack 的題目。但看了 Editorial 簡介，講到DP
# 我就用 DP 想想看：表格法：每次「多考慮」1個數，有 k 種可能 往回看  (bottom-up)
# 也可用「函式呼叫函式」慢慢增加「開始」的位置，各有 k 種可能 往右問 (top-down)
# 因 k<=500 這個迴圈不會跑太多次
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        N = len(arr)
        @cache
        def helper(start): # 從 start 往右，答案是什麼
            if start==N: return 0 # 終止條件：最右邊沒數字，最右邊的ans是0

            currMax = 0 # 現在這輪的最大值。隨著 i 增加，它也可能變大
            ans = 0 # 從 start 到最右邊，helper(start) 最大的ans是多少
            for i in range(start, min(N, start+k)): # 隨著k種可能 往右問
                currMax = max(currMax, arr[i]) # 這輪的最大值
                # [start,i] 是 currMax*(i-start+1), [i+1,...] 是 helper(i+1)
                ans = max(ans, currMax*(i-start+1) + helper(i+1))
            return ans

        return helper(0)
