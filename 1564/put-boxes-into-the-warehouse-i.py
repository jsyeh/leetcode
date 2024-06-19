# LeetCode 1564. Put Boxes Into the Warehouse I
# 將 boxes[i] 塞入 warehouse 裡，但如果高度不足，就無法塞入
# 使用 Editorial 的方法2，從左到右攞。如果高度不足，要更新H高度
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        boxes.sort(reverse=True) # 大的在左、小的在右
        i, j = 0, 0
        M, N = len(boxes), len(warehouse)
        ans = 0
        H = warehouse[0]
        while i<M and j<N:
            H = min(H, warehouse[j])
            if boxes[i]<=H:  # 剛好可塞入
                i, j = i+1, j+1
                ans += 1
            else: # 這個 boxes[i]無法塞入，換更小的
                i += 1
        return ans
