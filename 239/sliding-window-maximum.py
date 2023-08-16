# 題目不是找最大值，而是找「每個sliding windows」裡的最大值
# 一開始我看成找「sliding window」裡的總和。後來又誤以可用PriorityQueue解
# 最後用 Editorial 裡deque解法來解 (能從最前面取，能從最後面取) 查「霸主是誰」
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        N = len(nums)
        ans = [0]*(N-k+1) # 放答案的陣列，長度剛好是N-k+1 種樹問題

        # from collections import deque 應該LeetCode幫忙加了
        king = deque() # 王者、霸主，最左邊 dq[0]最大。移除後，新霸主會繼位
        # 能使用 dq.append(), dq.pop(), dq.popleft(), dq[0], dq[-1]
        
        for i in range(k): # 先把第1個 sliding window 建立 deque
            while len(king)>0 and nums[i] > king[-1]: # 塞入原則
                king.pop() # (2) (新)大的，會清掉前面(舊的)小的霸主繼承者
            # 取代成為新霸主的繼承者候選人 （如果繼承者候選人空了，就直接上）
            king.append(nums[i]) # (1) 舊的在左邊、新的(次大的)在右邊
        # 這樣便能確定 king[] 裡 (1) 舊的在左邊、新的(次大的)在右邊
        # (2) 在塞入時，(新)大的，會清掉前面(舊的)小的，取代成為新霸主
        # 這樣舊的大的離開後，新的/剩下裡面相對大的，便會露出來
        ans[0] = king[0] # 最左邊霸主（舊的、最大的）

        for i in range(k, N): # 後續，逐步移動 sliding window
            # 準備要移除的是：往左數k格的 nums[i-k]
            if nums[i-k] == king[0]: # 最左邊待移除的，剛好是現在的霸主
                king.popleft() # 舊霸主就被移除，將露出新霸主
            # 接著要塞入 nums[i] 這個數，同前面 
            while len(king)>0 and nums[i] > king[-1]: # 塞入原則
                king.pop() # 塞入原則：右邊塞入新數前，先把能取代的都先丟掉
            king.append(nums[i]) # 未來可能露出的新霸主塞進去
            ans[i-k+1] = king[0] # 最左邊的霸主
        return ans

