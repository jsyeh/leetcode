# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        N = len(lists)
        ans = ListNode()
        next = ans
        while True:
            nextI = -1
            for i in range(N):
                if lists[i] != None:
                    if nextI ==-1 or lists[i].val < lists[nextI].val:
                        nextI = i
            if nextI == -1: break # 沒有剩下任何 lists[i]!=None能用
            
            next.next = lists[nextI]
            lists[nextI] = lists[nextI].next
            next = next.next
        return ans.next
