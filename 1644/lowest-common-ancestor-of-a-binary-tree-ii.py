# LeetCode 1644. Lowest Common Ancestor of a Binary Tree II
# 在 tree 裡，找到 p 和 q 這兩個 nodes 的「共同祖先」node
class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 如果「左邊」有1個、「右邊」有1個，那就是答案
        def helper(root, p, q):
            if root==None: return None, 0  # 空的，什麼都沒有
            count = (root.val == p.val or root.val == q.val)  # 本身root是否有1
            node1, count1 = helper(root.left, p, q)  # 左半樹，累積結果
            if count1==2: return node1, count1  # 剛好有答案，就送上去

            node2, count2 = helper(root.right, p, q)  # 右半樹，累積結果
            if count2==2: return node2, count2  # 剛好有答案，就送上去

            if count1 + count2 + count == 2: return root, 2  # 湊齊2人，那root是答案
            return None, count1+count2+count
        node, count = helper(root, p, q)  # 函式呼叫函式，去找答案
        if count<2: return None  # 沒有找齊2個node，就失敗
        return node
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
