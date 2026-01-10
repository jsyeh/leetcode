# LeetCode 199. Binary Tree Right Side View
# 將 binary tree 橫向壓扁，每層的「最右邊」串起來、當答案
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        def helper(root, level):  # 利用「函式呼叫函式」解 tree 問題
            if root==None: return  # 遇到空的末稍，就結束
            if len(ans)<=level:  # 如果 ans 層數不夠
                ans.append(root.val)  # 就新增一層
            else:  # 如果層數夠
                ans[level] = root.val  # 就持續更新
            helper(root.left, level+1)  # 函式呼叫函式
            helper(root.right, level+1)  # 函式呼叫函式
        helper(root, 0)  # 啟動「函式呼叫函式」
        return ans
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
