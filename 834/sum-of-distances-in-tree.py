# n 個點，回傳 ans list 長度為 n, ans[i] 對應 node i 到全部點的距離總和
# 因 n<=3*10^4 所以不能暴力去試。
# Editorial 裡的解法，是先做一個tree，再把 tree 變形
# lee215 也是用一樣的解法。所以這題又學到了新的作法，太好了！
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        count = [1] * n  # 以 0 當 root 時，node i 下面「有幾個 node」（包含i本身），先預設1
        ans = [0] * n  # 先算出 ans[0] 的值，再由 ans[0] 推算鄰居的 ans[i]

        neighbor = defaultdict(set)  # 先由 edge 建出 neighbor的資料結構
        for a, b in edges:
            neighbor[a].add(b)
            neighbor[b].add(a)

        def dfs(root, parent):  # 先把 root 的答案ans[0]算出來，同時把 count[i] 算出來
            for i in neighbor[root]:
                if i != parent:
                    dfs(i, root)
                    count[root] += count[i]  # 把 i 以下的點，也算出 root 的小孩
                    ans[root] += ans[i] + count[i]  # i以下的點的數量，長度都再加1，便是 root 這層的貢獻
 
        def dfs2(root, parent):  # 由 ans[0] 推算出鄰居的 ans[i]
            for i in neighbor[root]:
                if i != parent:
                    ans[i] = ans[root] - count[i] + (n - count[i])
                    # ans[i] 由 ans[root] 推算：「減掉」下面的節點數count[i]，「加上」另一邊的節點數
                    dfs2(i, root)
        dfs(0, -1)  # 先算出 ans[0] 及 count[i]
        dfs2(0, -1)  # 利用 ans[0] 及 count[i]
        return ans

