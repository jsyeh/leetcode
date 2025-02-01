# LeetCode 2246. Longest Path With Different Adjacent Characters
# n nodes (0..n-1) 建出來的 tree 可用 parent 陣列「表示每個node的parent是哪個node」
# ex. parent[0] = -1 代表 node 0 沒有 parent
# parent[1] = 0 代表 node 1 的 parent 是 node 0
# 要從 tree 裡，找出「最長的PATH」而且「對應的字串」相鄰的字母「都不同」
# 可以把「相鄰字母相同」的edges都殺掉，再做2次BFS（第1次找最遠的點，第2次從最遠的點，找
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        N = len(parent)  # 目前有 N 個 nodes
        children = defaultdict(list)  # 先建立 parent 往 children 的 graph
        for i in range(N):
            children[parent[i]].append(i)  # 從 parent 往 children
        # Hint 2: 找「最小」的 child 長度（必須與root不同），但會超時，所以加上cache
        @cache
        def maxChildLen(root):  # 「從 root 出發」，找「往下最長」的children 長度
            ans = 0
            c0 = s[root]  # 先找 root 對應的字母 c0，不能與 child 相同
            for child in children[root]:  # 每個小孩，都找一次
                if s[child]==c0: continue  # 往下「不能相同」，如果字母相同，就不考慮
                ans = max(ans, maxChildLen(child))  # 更新「最大」的長度
            return ans + 1  # 要加上「自己本身」
        @cache
        def helper(root):  # Hint 1 從 root DFS，找 2 個 substree 間的最長距離
            # Part 1: 「最長」的 path 以 root 為「最高點/轉折點」
            ans = 1
            c0 = s[root]  # 先找 root 對應的字母 c0，不能與 child 相同
            branch = []  # 合理的 child branch 的長度放這裡
            for child in children[root]:  # 每一個小孩，看它的字母是否與 c0 不同
                if s[child]==c0: continue  # 往下「不能相同」，如果字母相同，就不考慮
                branch.append(maxChildLen(child))
            branch.sort(reverse=True)  # 大到小排好
            if len(branch)==1: ans = branch[0]+1  # 只有1條合理的 branch
            elif len(branch)>1: ans = branch[0] + 1 + branch[1]  # 最長的2條 branch
            # Part 2: 「最長」的 path 在其中一個 child 裡面，不關 root 的事
            for child in children[root]:
                ans = max(ans, helper(child))
            return ans
        return helper(0)
# case 8/142: [-1] "z"
# case 13/142: 很大量的 nodes 會超時。加上 @cache 就成功了!
