# LeetCode 1110. Delete Nodes And Return Forest 把 tree 裡 node 刪掉會變成 forest，但那是什麼？ 
# a forest is a disjoint union of trees 原來就是一堆樹的意思。所以樹被斷開時，就拆成許多部分。
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        to_delete = set(to_delete)  # 轉成 hash set 方便快速找元素
        ans = []  # travel()函式裡，斷開的答案，會被塞進來
        def travel(root):
            if root==None: return None  # 沒有東西
            if root.val in to_delete:  # 這裡要斷開，那它的兩個小孩，分別都是答案
                now = travel(root.left)  # 這兩行很像
                if now != None: ans.append(now)
                now = travel(root.right)  # 這兩行很像
                if now != None: ans.append(now)
                return None  # 本身消失
            root.left = travel(root.left)  # 左右的小孩「更新」後，再接回來
            root.right = travel(root.right)
            return root
        now = travel(root)  # 這兩行很像
        if now != None: ans.append(now)
        return ans
