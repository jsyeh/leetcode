# LeetCode 2322. Minimum Score After Removals on a Tree
# n 個 tree nodes (0..n-1) 對應值是 nums[i]，用 n-1 條 edges 相連
# 若刪掉 2 條 edges，原本的 tree 就會被「切成3塊」，「3塊」的對應值是「裡面成員xor的結果」
class Solution:  # 希望 3塊的 max(xor) - min(xor) 要最小
    def minimumScore(self, nums: List[int], edges: List[List[int]]) -> int:
        path = defaultdict(list)
        for a, b in edges:  # 先建立 path 資料結構
            path[a].append(b)
            path[b].append(a)
        childs = [set([i]) for i in range(len(nums))]  # 準備所有的小孩
        def buildTree(a):  # 函式呼叫函式：DFS 建樹，並將「雙向」path成「上到下單向」
            for b in path[a]:  # 本來平躺的 tree，把 node 0 拉起來，會變「直立」的 tree
                path[b].remove(a)  # 把另一個方向「刪除」變單向
                buildTree(b)  # 函式呼叫函式
                childs[a] |= childs[b]  # 爸爸的集合，包含小孩的集合
        buildTree(0)  # 函式呼叫函式，將 path 變成「單向」的 tree 從 0 出發
        stXOR = [num for num in nums] # 會記錄 subtree 的 XOR 值
        def findTreeXOR(a):  # 函式呼叫函式：找到 subtree 的 XOR 值
            for b in path[a]:
                stXOR[a] ^= findTreeXOR(b)  # 把 subtree 的 XOR 也算進來
            return stXOR[a]  # 整個 subtree 的 XOR 值
        findTreeXOR(0)  # 函式呼叫函式
        ans = inf  # 接下來「暴力for迴圈」找2個「刪掉兩edge後」的新 leader nodes
        for a in range(1, len(nums)):
            for b in range(a+1, len(nums)):
                if a in childs[b]:  # a 藏在 b 的下面，3個群便是 0, b, a
                    xor = [stXOR[0] ^ stXOR[b], stXOR[b] ^ stXOR[a], stXOR[a]]
                elif b in childs[a]:  # b 藏在 a 的下面，3個群便是 0, b, a
                    xor = [stXOR[0] ^ stXOR[a], stXOR[a] ^ stXOR[b], stXOR[b]]
                else:  # a b 互不隸屬, 所以 分開即可
                    xor = [stXOR[0] ^ stXOR[a] ^ stXOR[b], stXOR[a], stXOR[b]]
                ans = min(ans, max(xor) - min(xor))
        return ans
