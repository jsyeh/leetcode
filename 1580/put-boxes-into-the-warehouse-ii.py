# LeetCode 1580. Put Boxes Into the Warehouse II
# boxes[i] 高度，要推到 warehouse 裡面（從左or從右）
# 高度不夠時，就會卡住、不能再往內推。問最多可塞入幾個boxes
# 使用 Editorial 方法2: Add Largest Possible Boxes from Both Ends
# 
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        # 從大到小排序好，再從邊邊依序放入warehouse裡
        boxes.sort(reverse=True)
        ans = 0
        i, j1, j2 = 0, 0, len(warehouse)-1
        H1, H2 = warehouse[j1], warehouse[j2]
        while i<len(boxes) and j1<=j2:
            if H1<=H2: # 以大的為準，右邊大
                if boxes[i]<=H2: # 能放得下
                    ans += 1
                    j2 -= 1 # 右方再少一格
                    H2 = min(H2, warehouse[j2]) # 可能又變更矮了
            else: # 左邊大
                if boxes[i]<=H1:
                    ans += 1
                    j1 += 1 # 左方再少一格
                    H1 = min(H1, warehouse[j1]) # 可能又變更矮了
            i += 1 # 換下一個，再來塞塞看
        return ans


