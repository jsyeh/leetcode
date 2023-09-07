# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        '''
        ans = ListNode(0, head)
        prev, curr = ans, head # 一前一後
        for i in range(left-1): # 不交換的點
            prev, curr = curr, curr.next
        # 希望現在 prev, curr 剛好跨在 left左邊, left 的位置
        before = prev 
        for i in range(right-left+1): # 把要交換的點，都走過
            next, curr.next = curr.next, prev
            prev, curr = curr, next
        before.next.next = curr # 要看 Editorial Video 07:28 的接法
        before.next = prev # 要看 Editorial Video 07:28 的接法
        return ans.next
        # 1->2........v
        #       3<-4<-5
        #       ........>6->7->
        '''
        ans = ListNode(0, head) # 最後的答案會是 ans.next
        prev, curr = ans, head # 前面一格, 中間一格
        for i in range(left-1): # 要少走1格，因為是 1-index
            prev = prev.next # 順順往後走
            curr = curr.next # 順順往後走
        # 走到了 left ，準備要轉換後面的結果
        print(prev.val, curr.val)
        
        before = prev # 等一下要接到最後一筆的curr
        for i in range(left-1, right): # (left,right)有幾個，就走幾步
            # 每一次都要將方向調頭轉向
            next = curr.next # 備份下一步的位置
            curr.next = prev # 轉向
            prev = curr # 往下走
            curr = next # 往下走
        before.next.next = curr
        before.next = prev # 讓 before 接到righ的那一筆
        return ans.next
        
