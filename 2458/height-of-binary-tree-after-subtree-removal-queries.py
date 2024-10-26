# LeetCode 2458. Height of Binary Tree After Subtree Removal Queries
# 砍樹問題：樹的 node 1...n 共 n nodes。把 val 為 queries[i] 的 node 砍掉。
# 問你「砍掉後，樹高度 height」（砍完又要復原）。這題很難，樹很大，容易超時。
# Solutions 裡 Bakerston 寫得很好，可參考它的解說、畫圖。某段「被砍掉」後，互相獨立的同層鄰居，可取代（被砍掉的部分）
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        Above, Below = {}, {}  # 每個 node 「上到中」及「中到下」的長度
        def depth(root, level):  # 進行 depth 分析，找出每個node的 above 及 below 的長度
            if root==None: return -1  # 終止條件。下面層數「要減掉自己」所以-1
            Above[root.val] = level  # 上到中：有幾層？
            ans = max(depth(root.left, level+1), depth(root.right, level+1)) + 1  # 函式呼叫函式
            Below[root.val] = ans # 中到下：子孫最遠到有多長？（砍樹時要更新）
            return ans

        depth(root, 0)  # 試著將全部「上到中」「中到下」都先算出來

        sameLevelBrother = defaultdict(list)  # 在同一層的表兄弟遠親近親
        for node, below in Below.items():  # 每個node 對應的 below長度
            level = Above[node]  # 上到中，有幾層?
            sameLevelBrother[level].append((Below[node],node))  # 更新「某層」往下「有哪些可能的深度」
            sameLevelBrother[level].sort(reverse=True)  # 大到小排好
            if len(sameLevelBrother[level]) > 2:  # 每次砍完「會還原」，只要記2筆：砍最大（用次大） or 沒砍最大（用最大）
                sameLevelBrother[level].pop()  # 只留「最大」的2筆

        ans = []
        for query in queries:
            level = Above[query]  # 上到中，有幾層?
            if len(sameLevelBrother[level])==1:  # 關鍵的唯一，若砍掉，就斷了
                ans.append(level-1)  # 因砍掉，再短1層
            elif sameLevelBrother[level][0][1]==query:  # 剛好砍掉「最大的」
                ans.append(sameLevelBrother[level][1][0] + level) # 第2大的補上
            else: # 沒有砍到「最大的」
                ans.append(sameLevelBrother[level][0][0] + level) # 就用「最大的」
        return ans

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

