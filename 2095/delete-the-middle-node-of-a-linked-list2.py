# LeetCode 2095. Delete the Middle Node of a Linked List
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None: # 特殊狀況：只有1個的話
            return None # 那就要殺掉它，剩下 None
        fast = slow = prev = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            prev = slow
            slow = slow.next
        prev.next = slow.next
        return head
