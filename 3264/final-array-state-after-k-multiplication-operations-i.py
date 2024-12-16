# LeetCode 3264. Final Array State After K Multiplication Operations I
# 進行 k 次操作：找最小值，把它乘上 multiplier 再放回去
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num,i) for i,num in enumerate(nums)] 
        heapify(heap)  # 把原本 nums[i] 及 i 放入 heap，方便「取出小的」
        for kk in range(k):  # 進行 k 次操作
            num, i = heappop(heap)  # 取出最小的數，附上 index i
            nums[i] = num * multiplier  # 乘好後，再放回去 nums[i]
            heappush(heap, (nums[i],i))  # 再更新 heap 內容
        return nums
        
