# LeetCode 2058. Find the Minimum and Maximum Number of Nodes Between Critical Points
# 今天的題目，又是 Linked List 資料結構題，「local最大值」比左右鄰居大； 「local最小值」比左右鄰取小
# 想要找到「local 最大/最小值」的最小距離、最大距離。
# 最小距離，就逐「小段」比較，最大距離，就是最前、最後的local極值
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        prev, now, next, i = head, head.next, head.next.next, 1
        pos = [] # 用來放 local最大值/最小值 的 index 位置
        while next != None: # 整個 linked list 巡一次，建出「區域極值」的位置
            if now.val > prev.val and now.val > next.val: # local最大值
                pos.append(i)
            elif now.val < prev.val and now.val < next.val: # local最小值
                pos.append(i)
            prev, now, next, i = prev.next, now.next, next.next, i+1 # 換下一筆, 並更新 index
        # 建好pos區域極值的位置後，再巡一次，了解全部的距離。這部分可整合到上面加速
        if len(pos)<2: return [-1,-1]
        distMax = pos[-1] - pos[0]
        distMin = pos[1] - pos[0]
        for i in range(len(pos)-1):
            distMin = min(distMin, pos[i+1]-pos[i])
        return [distMin, distMax]

