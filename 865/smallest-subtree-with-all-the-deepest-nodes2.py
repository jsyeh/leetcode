# LeetCode 865. Smallest Subtree with all the Deepest Nodes
# 找到最深的 deepest nodes 後，把全部包含的最小的 subtree 找出來
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def helper(root, level):  # 把兩個「函式呼叫函式」併成一個
            if root==None: return 0, None  # 兩個答案: 深度、subtree
            depth1, subtree1 = helper(root.left, level+1)
            depth2, subtree2 = helper(root.right, level+1)
            # 接下來，看要相信誰：比較深的那個，對應的 subtree 是答案
            if depth1 > depth2:  # 左邊比較深
                return depth1 + 1, subtree1
            if depth1 < depth2:  # 右邊比較深
                return depth2 + 1, subtree2
            # 那兩邊一樣深，就代表「你本人」就是答案
            return depth1 + 1, root  # 「你本人」就是答案
        depth, subtree = helper(root, 0)
        return subtree
