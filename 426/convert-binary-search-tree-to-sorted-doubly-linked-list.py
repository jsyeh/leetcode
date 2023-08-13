"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        '''
        if root == None: return root # 測試確認可這樣寫
        if root.left==None and root.right==None:
            root.left = root
            root.right = root
            return root # 測試可這樣寫，讓我了解資料的接法
        '''

        head = Node() # 照題目的圖示
        # head 的右邊，會指最小的數
        # head 的左邊，會指（目前）最大的數
        
        def helper(root):
            if root == None:
                return
            left, right = root.left, root.right
            # 先備份左右，因為中間會修改它們

            helper(left)

            # 如果第一次看到節點，要記得接到head
            if head.left==None: head.left=root
            if head.right==None: head.right=root
            biggest = head.left
            smallest = head.right
            root.left = head.left # 接上目前最大的數
            root.right = head.right # 接上目前最小的數
            biggest.right = root
            smallest.left = root
            # root將是現在(剛誕生)最大的數哦
            head.left = root # 接上新的（最大）node
            
            helper(right)
                
        helper(root)
        return head.right # 目前最小的數
