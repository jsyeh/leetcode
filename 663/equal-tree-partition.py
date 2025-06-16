# LeetCode 663. Equal Tree Partition
# 要把 tree 分成 2 個 tree 而且裡面加起來的總合相同。
# 可先查「總和」，再看哪個 subtree 剛好「總和是一半」即可
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        def countSum(root):  # 用「函式呼叫函式」先算出全部的「總和」
            if root==None: return 0
            return countSum(root.left) + countSum(root.right) + root.val
        def foundSum(root, target):  # 用「函式呼叫函式」，查看「總和」是否是 target 值
            # 查看「本 subtree 裡」，是否有人的 sum 是 target？目前 sum 是多少? (答案藏了2個值)
            if root==None: return False, 0
            leftSuccess, leftSum = foundSum(root.left, target)  # 左半樹的狀況
            rightSuccess, rightSum = foundSum(root.right, target)  # 右半樹的狀況
            now = leftSum + rightSum + root.val
            if now == target: return True, now
            return (leftSuccess or rightSuccess), (leftSum+rightSum+root.val)  # 左小樹、右小樹，有沒有人成功？
        total = countSum(root)  # 算算出全部的「總和」
        if total % 2 != 0: return False  # 奇數、不能分成一半，失敗
        return foundSum(root.left, total // 2) [0] or foundSum(root.right, total // 2) [0]
        # 用「函式呼叫函式」看能不能找到「剛好一半」的 target 目標

# 特別的 case
# case 193/198: [0,-1,1]
# case 188/198: [1,-1]  # 如果誤以為 null child 是 subtree 就會出錯，要注意
