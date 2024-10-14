# LeetCode 2530. Maximal Score After Applying K Operations
# 模擬題：nums[i] 挑1個數，分數score += nums[i], 把 nums[i]=ceil(nums[i]/3)
# 也就是「每次挑個數」後，那個數會變小，而分數score會增加。想要最多的分數score。
# 可用 Priority Queue (Heap) 來解這題，只要再加「負號」就能順利模擬
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        heap = [-num for num in nums]  # 用「負號」將數字都變負數
        heapify(heap)  # 再建出 Heap 資料結構，能隨時/快速取最小值（對應原本最大值）
        score = 0
        for i in range(k):  # 做 k 次模擬
            now = -heappop(heap)  # 現在取出「原本最大值」（即heap的最小值，再負號）
            score += now  # 照題目描述，增加score
            heappush(heap, -ceil(now/3))  # 照題目描述，取 ceil(now/3)，再負號放進heap
        return score
