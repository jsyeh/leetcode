# 這題剛看好像很難，在想是不是要壓扁變成 list 再去數數
# 不過突然想到 BST 可用函式呼叫函式的方式，就可小到大依序找出來
# 後來想到 https://www.youtube.com/watch?v=pKO9UjSeLew
# If Programming Was An Anime 裡面有用 sort()也有用HashMap
# 就用 HashMap 吧！
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        d = defaultdict(int) # 字典
        def helper(root):
            if root==None: return
            helper(root.left)
            d[root.val] += 1
            helper(root.right)

        helper(root)
        m = max(d.values()) # 最多的數量

        ans = []
        for key in d: # 再把字典裡，每個key都巡
            if d[key]==m: # 剛好數量是最大的m
                ans.append(key) # 此key就是答案(之一)
        return ans

