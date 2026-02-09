# LeetCode 1382. Balance a Binary Search Tree
# 要把 binary search tree 變 balance (每個node左右深度最多差1)
# 可先把 binary search tree 變成 array, 再二分法變回tree
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        a = []  # array 陣列
        def buildArray(root):  # 題目 Hint 建議「先變成 array 再變成 tree」
            if root==None: return
            buildArray(root.left)  # 函式呼叫函式
            a.append(root.val)  # 利用 in-order 將資料放入陣列 a
            buildArray(root.right)  # 函式呼叫函式
        buildArray(root)  # 將 binary search tree 變 array
        
        def buildTree(left, right):  # 左包含、右不包含
            if right-left<1: return None  # 沒辦法構成
            if right-left==1: return TreeNode(a[left])
            mid = (left+right)//2  # 中間的點，當 root
            return TreeNode(a[mid], buildTree(left, mid), buildTree(mid+1, right))
        return buildTree(0, len(a))
