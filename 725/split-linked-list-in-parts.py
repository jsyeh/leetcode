# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 要裝 Linked List 分成 k parts，所以要先知道全長
        N = 0
        head2 = head
        while head2!=None:
            head2 = head2.next
            N += 1
                # 接下來除法，算出有幾個
        avg, more = N // k, N % k # 前 more 個有 avg+1 個，其他 avg個

        ans = [] # 用來裝 k 個答案
        for i in range(more): # 每個都有 avg+1 個
            ans.append(head)
            prev = head
            for j in range(avg+1):
                prev = head # 用來最後「斷後用」
                head = head.next
            prev.next = None # 「斷後」

        for i in range(k-more): # 每個都有 avg 個
            if avg==0: # 遇到長度是0的，例外處理
                ans.append(None) # 因「斷後」會出錯，所以這裡才要例外處理
                continue
            ans.append(head)
            prev = head # 這寫法有問題，因這裡不是真的 prev，「斷後」會出錯
            for j in range(avg):
                prev = head # 用來最後「斷後用」
                head = head.next
            prev.next = None # 「斷後」

        return ans
