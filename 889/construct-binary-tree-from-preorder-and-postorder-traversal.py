# LeetCode 889. Construct Binary Tree from Preorder and Postorder Traversal
# 用 Preorder 和 Postorder 分別走過的結果，推導出原始的 tree
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # 先建出「快速找到 index 位置」的對照表
        preIndex = { v:i for i,v in enumerate(preorder) }
        postIndex = { v:i for i,v in enumerate(postorder) }

        def helper(i, L):  # 函式呼叫函式，給 root 起點i 及 長度L，建出小樹
            root = preorder[i]  # 把「起點i」的 root 值取出
            ans = TreeNode(root)  # 建出對應「小樹」的 root 當答案
            if L==1: return ans  # 若剛好「長度L」是1，就這個 TreeNode 已是答案，送出

            left = i + 1  # 左邊的小樹，是由 preorder 的 i+1 開始
            right = preIndex[postorder[postIndex[root]-1]]  
            # 右邊的小樹，去查 postorder 的 root 位置的前一格，取出它的值，再去問 preIndex 這個值在哪裡
            if left==right:  # 若「左邊的小樹」，和「右邊的小樹」其實是同一個樹，就掛在左邊就好
                ans.left = helper(left, L-1)  # 就掛在左邊就好
            else:  # 兩個分開的小樹
                ans.left = helper(left, right-left)  # 掛好「左邊的小樹」，用對應的「長度」函式呼叫函式
                ans.right = helper(right, L-1-(right-left))  # 掛好「右邊的小樹」，用對應的「長度」函式呼叫函式
            return ans  # 掛好左右的小樹後，就建出小樹了！
        return helper(0, len(preorder))  # 現在，從頭開始「建出完整」的樹

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

