# 希望node可（頭尾）交錯串起來
# 可先將後半找出來、後半反轉，最後「交錯」串起來
# 最重要的，是「不可以return」，直接修改 head 後面的串接結構
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        fast = slow = head # 龜兔賽跑，fast slow 找中間點
        while fast.next!=None and fast.next.next!=None:
            # 上面的條件，會少走1格，讓slow.next 才是後半段
            fast = fast.next.next
            slow = slow.next
        # 離開迴圈時，代表slow.next是後半段的頭
        second = slow.next # 第二段
        slow.next = None # 將前半段「剪斷」
        # 再把後半段「反過來」
        rev = None # 將會放「第二段」反過來的結果
        while second != None:
            # 先列出3個要改的東西: slow, slow.next, rev
            # 口訣有點像 A,B,C 三個數字轉一圈交換
            temp = second.next
            second.next = rev
            rev = second
            second = temp
        # 再將 head 及 rev 合併(「交錯」串起來)
        head1, head2 = head, rev
        while head1!=None:
            # head1的下一筆是 head2 而 head2 改到樓上
            head1.next, head2 = head2, head1.next
            head1 = head1.next # 往下走一格，接手 head2的位置
        return 
