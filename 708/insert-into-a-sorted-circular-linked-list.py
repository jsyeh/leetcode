"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Optional[Node]', insertVal: int) -> 'Node':
        if head == None: # 遇到空Node，就補Node
            ans = Node(insertVal)
            ans.next = ans
            return ans
        
        next = head
        min, max = head.val, head.val
        while True: # 巡過一輪
            if next.val > next.next.val: # 逆行時，就是頭尾相接
                max = next.val
                min = next.next.val
                break # 找到頭尾相接的地方
            next = next.next 
            if next == head: break # 迴圈重覆時，便可離開了
        pos = next # 找到「頭尾相接」的地方（也就是正負逆行的地方)
        if insertVal > max or insertVal < min: # 若插入值更大 or 更小
            temp = Node(insertVal, pos.next)
            pos.next = temp # 就直接插在「頭尾相接」的地方
            return head

        next, prev = head.next, head
        while True: # 迴圈一直做
            if prev.val <= insertVal and insertVal <=next.val:
                now = Node(insertVal, next)
                prev.next = now
                break # 找到插入點：數字夾在中間
            # 沒有離開的話，就繼續循還
            prev = prev.next
            next = next.next
        return head
# case 104/108: [3,3,5] 0 不小心插入「相同數字夾起來的地方
# 所以要知道 [3,3] 與 [3,3,5] 對0的插入法不同。
# case :[5,1,3] 2
