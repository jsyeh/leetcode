# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        def helper(root: Optional[TreeNode]) -> str:
            if root == None: return "" # 沒東西，就空字串
            ans = str(root.val) + "," # 數字結尾都是逗號
            ans += helper(root.left) # 根據 BST, 左邊都小
            ans += helper(root.right) # 根據 BSt, 右邊都大
            return ans # 字傳接起來，return

        # 有了 helper()幫忙，便能「函式呼叫函式」拆解變字串
        ans = helper(root)
        # print(ans)
        return ans        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        nums = deque() # 想要使用 append() 及 popleft() 與 nums[0]
        for s in data.split(","): # 斷字，再逐字取出
            # print(s)
            if s != "": # 只要不是最後的空字串
                nums.append(int(s)) # 轉成數字, 加入 nums

        # helper() 會幫忙，把 deque 取出 nums[0] 或 popleft()
        def helper(nums: collections.deque, left: int, right: int)->Optional[TreeNode]:
            if len(nums)==0: return None # nums 都取光時，便應結束
            val = nums[0]
            if val < left or right < val: return None # 數字超過BST子樹的範圍，便應結束

            # print("val:", val, left, right)
            ans = TreeNode(val) # 照著子樹的 root.val 建 子樹
            nums.popleft() # 把 root.val 丟掉，以便下面分別 parse取用
            ans.left = helper(nums, left, val) # 在新的左右範圍內的，才建子樹
            ans.right = helper(nums, val, right) # 在新的左右範圍內的，才建子樹
            return ans # 將現在的樹傳出去
        return helper(nums, -1, 99999) # 因 val 介於 0...10^4, 決定左右範圍
        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
