# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 使用 merge sort 來解決此題，先搞定終止條件
        if head==None or head.next ==None: return head

        # 接下來利用 fast,slow 來找到中間點
        fast, slow, prev = head, head, head
        while fast!=None and fast.next!=None:
            fast = fast.next.next
            prev = slow # 備份，以便等一下要斷開
            slow = slow.next
        # 離開迴圈時, slow是中間點
        prev.next = None # 斷開，讓head只有前半斷
        list1 = self.sortList(head)
        list2 = self.sortList(slow)

        # Merge
        ans = ListNode()
        next = ans
        while list1!=None and list2!=None:
            if list1.val < list2.val:
                next.next = list1
                list1 = list1.next
                next = next.next
            else:
                next.next = list2
                list2 = list2.next
                next = next.next
        if list1==None:
            next.next = list2
        else:
            next.next = list1
        return ans.next
