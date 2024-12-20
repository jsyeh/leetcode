# LeetCode 2415. Reverse Odd Levels of Binary Tree
# tree 是完整的，裡面奇數層要左右對調。用「函式呼叫函式」應可解決
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        oddLevel = []  # 裡面會放「奇數層」裡面全部的值
        def buildOddLevel(root, level):
            if root==None: return  # 樹末梢（盡頭）
            if level%2==1:  # 奇數層 (最上面那層)
                if len(oddLevel)<=level:
                    oddLevel.append([])  # 想讓程式看起來漂亮，所以一次補2次
                    oddLevel.append([])  # 讓程式可以用 oddLevel[level] 直接存取，不用寫 oddLevel[level//2]
                oddLevel[level].append(root.val)  # 把奇數層的值，放入 oddLevel[level] 裡面
            buildOddLevel(root.left, level+1)
            buildOddLevel(root.right, level+1)
        def changeOddLevel(root, level):
            if root==None: return
            if level%2==1:
                root.val = oddLevel[level].pop()
            changeOddLevel(root.left, level+1)
            changeOddLevel(root.right, level+1)
        buildOddLevel(root, 0)
        changeOddLevel(root, 0)
        return root
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

