# LeetCode 862. Shortest Subarray with Sum at Least K
# 在 nums 裡，找一段「最短的連續subarray」，加起來>=k。
# 但裡面有正、有負，不能用直覺的 sliding window 毛毛蟲法。要用 Mono Queue 配合deque() 來解
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        queue = deque()  # 裡面會放「重點位置」的 index 及 total 值，裡面total值會 Mono 漸增
        queue.append( (-1,0) )  # 左邊是 index i 位置，右邊是到 index i 的加總結果 total
        ans, total = inf, 0  # ans:最小值（長度），預設 inf 無限大, total:某段加起來的prefix sum
        for i, num in enumerate(nums):  # 現在處理到第 i 個數字 nums[i]
            total += num  # 把現在的數字，加入 total
            while len(queue)>0 and total - queue[0][1]>=k:  # 若最左邊/最遠的開始，加到i，加起來>=k
                ans = min(ans, i - queue.popleft()[0])  # 更新答案，同時吐掉它，下次再試稍微近的那個
            
            while len(queue)>0 and total <= queue[-1][1]:  # 要Mono漸增，能插入右端嗎？若無法壓入右邊
                queue.pop() # 就吐掉舊的右邊
            queue.append( (i, total) ) # 把現在的 index 及 total 資訊，正式插入左邊
        if ans==inf: return -1  # 沒更新過 ans，就是沒有解，回傳 -1
        return ans
