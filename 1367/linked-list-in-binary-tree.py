# LeetCode 1367. Linked List in Binary Tree
# tree 「從上往下」走，有沒有一條「內容和linked list相同」的路徑
# 用到2個技巧：(1)「函式呼叫函式」嘗試將每個點都當成「開始點」測試。
# (2) 再利用「函式呼叫函式」的dfs()看「開始點」之後的 linked list node 是否能在tree找到
class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        def dfs(head, root):  # 函式呼叫函式，照著 linked list 開始「逐層往下比對」
            if head==None: return True  # 成功走到 linked list 的最後
            if root==None: return False  # tree 無法測試到最後，失敗
            if head.val != root.val: return False  # 這層的 node 內容不同，失敗
            # 到達這裡，代表這層 node 內容相同，用 dfs() 繼續往下面比
            return dfs(head.next, root.left) or dfs(head.next, root.right)

        # 這裡是 isSubPath() 本人，用「函式呼叫函式」把每個點當「開始點」叫用 dfs()
        if head==None: return True  # 成功走到 linked list 的最後
        if root==None: return False  # tree 無法測試到最後，失敗
        if dfs(head, root): return True  # 從這裡開始，能順利比對成功，太好了!
        # 到達這裡，代表「這層 node 無法開始」，只能期待「下一層開始」
        return self.isSubPath(head, root.left) or self.isSubPath(head, root.right)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
