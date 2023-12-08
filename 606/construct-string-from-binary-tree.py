# 今天的題目, 是 LeetCode 很喜歡的 Binary Tree 風格的題目, 而且測試資料裡, 
# 也會把(資料結構裡)對應的 Tree 畫出來, 方便理解。
# Tree 的題目, 很常用「函式呼叫函式」的方法來解決。因為 樹 和它的左邊樹、右邊樹,長的結構都類似。
# 這題是把 root.val 的值準備好, 如果有左邊樹, 就 (左邊樹)。如果有右邊樹, 就(右邊樹)
# 如果沒有樹, 就連空括號都不要出來。
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root == None: return "" # 如果現在這棟樹是空的, 對應的字串是空字串, 提早結束

        now = str(root.val) # 現在這個root節點,對應的值的字串, 等一下要做字串加法
        left = self.tree2str(root.left) # 左邊的樹的字串, 還沒加括號
        right = self.tree2str(root.right)# 左邊的樹的字串, 還沒加括號
        
        if left=="" and right=="": return now # 如果左右的樹都空空的, 就只回傳 now 的值
        if right=="": return now + "(" + left + ")" # 如果右邊是空的, 就只加入左邊的樹
        return now + "(" + left + ")(" + right + ")" # 最後這條規則, 是完整全部送出
        # 有人會問, 那left空、right不空, 怎麼辦? 那就要 now()(right) 放個空的在左邊
