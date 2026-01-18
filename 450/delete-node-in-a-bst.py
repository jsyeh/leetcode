# LeetCode 450. Delete Node in a BST
# 在 binary search tree 裡, 把某個 node 刪掉, 並更新 tree 內容、保持BST結構
# 也就是「把左邊的最右邊」or「右邊的最左邊」放入原本node的位置
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def findLeftMost(root):  # 找到最左邊node的key
            if root.left == None: return root.val  # 沒有左邊，本身就是最左邊
            return findLeftMost(root.left)  # 有左邊，就再「函式呼叫函式」

        if root == None: return root
        if root.val == key:  # 需要刪掉此node
            if root.left == None and root.right == None:  # 沒小孩
                return None  # 可整個刪掉
            if root.right == None:  # 右邊沒有小朋友的話
                return root.left  # 可以把左邊提昇、取代自己
            else:  # 右邊有小朋友的話，去找右邊的「最左邊」
                key2 = findLeftMost(root.right)  # 將右邊的 leftMost
                root.val = key2  # 把它取代（被刪除的）本身
                # 再使用「函式呼叫函式」把右邊的小樹「去除key2」再接到右邊即可
                root.right = self.deleteNode(root.right, key2)
                return root  # 完成任務，結束
        # 如果現在這層還沒有找到的話，這層保留，同時左邊、右邊，都再「函式呼叫函式」
        root.left = self.deleteNode(root.left, key)
        root.right = self.deleteNode(root.right, key)
        return root
            
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
