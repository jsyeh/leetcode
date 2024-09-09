# LeetCode 2326. Spiral Matrix IV
# m x n 的矩陣，裡面的值，用 linked list 放在 head 裡，請做出矩陣
# 從「左上角」開始，撞到邊之後右轉，不夠的項放-1，照著模擬即可。
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        ans = [[-1]*n for _ in range(m)]  # 先預放「一堆-1」的矩陣
        i, j, d = 0, -1, 0  # 目前的位置、方向(0:右，1:下，2:左，3:上)
        # j 先預退1格（-1）之後再進1格，便是 0,0 的位置開始
        di, dj = [0,1,0,-1], [1,0,-1,0] # 4個方向，對應移動改變量
        while head != None:  # 如果 linked list 還有值
            ii, jj = i+di[d], j+dj[d]  # 預先走的index，方便測試轉向
            if ii<0 or jj<0 or ii>=m or jj>=n: # 撞到邊界，就轉方向
                d = (d+1) % 4  # 轉向
            ii, jj = i+di[d], j+dj[d]  # 預先走的index，方便測試轉向
            if ans[ii][jj]!=-1: # 如果前方有走過，就轉方向
                d = (d+1) % 4  # 轉向
            i, j = i + di[d], j + dj[d]
            ans[i][j] = head.val
            head = head.next
        return ans
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
