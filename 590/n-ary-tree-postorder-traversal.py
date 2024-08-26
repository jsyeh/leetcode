"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""
# LeetCode 590. N-ary Tree Postorder Traversal
# 資料結構裡，有很多小孩（不只是binary tree兩個小孩）
# 所以要用迴圈，把每個小孩都走過一次，最後才放自己本身的值
class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        ans = []  # 用來放答案
        def visit(root): # 用「函式呼叫函式」求答案
            if root == None: return  # 終止條件：走到末端
            for child in root.children:  # 每個小孩，都走一次
                visit(child)
            ans.append(root.val)  # 最後，放入自己本身的值
        visit(root)  # 程式從頭開始，跑一次
        return ans  # 算出的 ans 答案回傳
