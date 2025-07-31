# LeetCode 272. Closest Binary Search Tree Value II
# 在 BST tree 裡，找 k 個「最接近 target」的值
# 直覺會想到「把 tree 變成 array」就容易找。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestKValues(self, root: Optional[TreeNode], target: float, k: int) -> List[int]:
        def helper(root):  # 負責把 subtree 變成 array
            if root==None: return []
            else: return helper(root.left) + [root.val] + helper(root.right)
        arr = helper(root)  # 先把 tree 變成 sorted array
        print(arr)
        i = bisect_left(arr, target) - 1
        a, b = i, i+1  # a 往左、 b 往右
        if i==-1:
            a, b = i+1, i+2
        ans = []
        while len(ans) < k:
            print('a', a, 'b', b)
            if b==len(arr) or abs(target - arr[a]) < abs(arr[b]-target):  # b到底 or a較近 (要有 abs() 才能避免 a==-1 的狀況)
                ans.append(arr[a])  # 要往 a 方向發展
                a -= 1  # a 往左
            else:  # 要往 b 方向發展
                ans.append(arr[b]) # 往 b 方向發展
                b += 1  # b 往右
        return ans
