# 想把「linked list」裡的數，逐一數「出現次數」
# 再把這些「出現次數」放到 linked list 裡回傳。
# 本題 Hint 1 建議用 HashMap, 所以我用 Counter()
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def frequenciesOfElements(self, head: Optional[ListNode]) -> Optional[ListNode]:
        counter = Counter() # 準備好 Counter()
        while head!=None: # 針對 head 的 linked list 全走一次
            counter[head.val] += 1 # 計算出現次數
            head = head.next # 下一筆
        ans = now = ListNode() # 準備答案的 linked list (最前面不用)
        for n in counter: # 將 counter 裡每個 key 逐一取出
            now.next = ListNode(counter[n]) # 將對應 value 存入 linked list 中
            now = now.next
        return ans.next # 避開「最前面不用」的 linked list 答案
