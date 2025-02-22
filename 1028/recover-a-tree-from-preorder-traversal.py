# LeetCode 1028. Recover a Tree From Preorder Traversal
# 資料結構演算法 tree preorder traversal 是把 tree 「左、中、右」走一次
# 題目給字串 traversal 裡面有數字、有'-'減號（代表「深度幾層」）
# 要反過來，要把整個 Tree 重建出來（題目說，優先建左邊的 tree）
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        table = [[] for i in range(1000)]  # 表格放每一層「正在處理中的 TreeNode」
        nodes = traversal.split('-')  # 利用 .split() 斷字，很多減號會變 ''
        # print(nodes)  # 把 "1-2--3--4-5--6--7" 斷成 ['1', '2', '', '3', '', '4', '5', '', '6', '', '7']
        table[0] = TreeNode(int(nodes[0]))  # root 放「最前面」的數字，整個樹的源頭
        D = 0  # 爸爸的層數
        for now in nodes[1:]:  # 避開剛剛用的 node[0], 從 nodes[1]開始建樹
            if now != '':  # 不是空的、「有數字」，就加到 table 裡
                table[D+1] = TreeNode(int(now))  # 「放入」新的下面那一層
                if table[D].left==None:  # 如果爸爸左邊沒有，放放左邊
                    table[D].left = table[D+1]  # 把「新的一層」掛在爸爸的左邊
                else:  # 左邊有，就放右邊
                    table[D].right = table[D+1]  # 把「新的一層」掛在爸爸的右邊
                D = 0  # 處理「有數字」，爸爸的層數又變回 0
            else: D += 1  # 是空的（減號會成變 ''），爸爸的層數就加1層
        return table[0]  # 整個樹的源頭 root （建好了，就是答案囉）
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
