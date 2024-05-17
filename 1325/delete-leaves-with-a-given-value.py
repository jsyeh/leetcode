# LeetCode 1325. Delete Leaves With a Given Value
# 摘除一些leaf葉子, 一直摘、一直摘, 直到不能摘。
# 利用函式呼叫函式, 在 TreeNode裡, 把某些值的 node 刪除, 再看自己是否變成葉子、要不要刪
# Definition for a binary tree node. 英文是資料結構的介紹
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val  值
#         self.left = left 左邊的小孩
#         self.right = right 右邊的小孩
class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        if root == None: return root  # 沒有東西,就提早結束
        left = self.removeLeafNodes(root.left, target)  # 先用同一個函式, 處理左半邊
        right = self.removeLeafNodes(root.right, target)  # 用同一個函式, 處理右半邊
        if left==None and right==None and root.val==target:  # 最後變葉子,且值同
            return None  # 什麼都沒有, 交給當初呼叫我的人 (就是把自己刪掉)
        
        root.left = left  # 把新的左邊刪後的結果,接到左邊
        root.right = right  # 把新的右邊刪後的結果,接到右邊
        return root  # 交回新的答案
