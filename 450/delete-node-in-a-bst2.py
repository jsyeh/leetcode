# LeetCode 450. Delete Node in a BST
# 在 binary search tree 裡, 把某個 node 刪掉, 並更新 tree 內容、保持BST結構
# 也就是「把左邊的最右邊」or「右邊的最左邊」放入原本node的位置
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        def helper(root):  # 找到左邊的最右邊
            if root.right==None: return root.val
            return helper(root.right)
        if root==None: return root
        if root.val == key:
            if root.left==None: return root.right  # 接右邊
            key2 = helper(root.left)
            root.val = key2
            root.left = self.deleteNode(root.left, key2)
            return root
        if root.left: root.left = self.deleteNode(root.left, key)
        if root.right: root.right = self.deleteNode(root.right, key)
        return root
