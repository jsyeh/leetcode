# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        N = 0
        Anya = head # 使用 Spy x Family 的梗圖，Anya 像指標，指下一個Anya
        while Anya != None:
            Anya = Anya.next
            N += 1
        
        Anya = head
        for i in range(int(N/2)):
            Anya = Anya.next
        
        return Anya
