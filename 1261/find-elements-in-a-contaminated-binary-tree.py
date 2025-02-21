# LeetCode 1261. Find Elements in a Contaminated Binary Tree
# 給一個 tree 照規則放 val:左邊是 x*2+1，右邊是 x*2+2
# 問 target 有沒有在 tree 裡。這題用 set() 記下每一個值，就完成了
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.exist = set()  # 存在的數，放在 self.exist 裡
        def build(root, x):  # 用「函式呼叫函式」把 tree 走一輪
            if root==None: return  # 走到末稍，結束
            # root.val = x  # 更新 node 的值（不更新，好像也可以）
            self.exist.add(x)  # 記下這個 node 的值
            build(root.left, x*2+1)  # 「函式呼叫函式」走左邊
            build(root.right, x*2+2)  # 「函式呼叫函式」走右邊
        build(root, 0)  # 從 root 出發，照規定放 0

    def find(self, target: int) -> bool:
        return target in self.exist

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
