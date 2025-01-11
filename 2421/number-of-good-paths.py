# LeetCode 2421. Number of Good Paths
# 有 n nodes 對應 n - 1 edges 的「軟趴趴躺在地上」的 tree
# 開始點、結束點 的 val 要相同，中間的值「不能更大」有幾條這樣的path?
# tree 任兩點，只有「唯一」的path。所以找「最大」的值有幾個，算出。斷開，再持續做。
class Solution:
    def numberOfGoodPaths(self, vals: List[int], edges: List[List[int]]) -> int:
        N = len(vals)
        ans = N  # 每1個node（自己）都可以是「合格」的path
        # 照 lee215 思緒，tree 裡 maxv 是無法跨越的障礙，用完要斷開 -- 
        # 作法反過來，從小到大長出來
        counter = [Counter({vals[i]: 1}) for i in range(N)]
        #  counter[i][vals[i]] 對應 node i 到「值是val[i]」的 path 有 1 條，都還沒接起來哦！
        edges = sorted([max(vals[i],vals[j]),i,j] for i, j in edges)
        # edge相接的2個node的vals[i]大的值，是上限，當key 從小到大排序，以便「小到大」取出，再慢慢「接起來」
        
        f = list(range(N))  # 每個人，一開始，是自己的主人
        def find(x):  # union-find 的過程
            if f[x] != x:
                f[x] = find(f[x])  # 進行 union-find 更新
            return f[x]  # 回傳新主人
        
        for val,i,j in edges:  # 照著 val 小到大取出，現在要結合「小集團i」「小集團j」成為「大集團
            fi, fj = find(i), find(j)  # 找各自的主人（的node id編號）「小集團fi」「小集團fj」
            ci, cj = counter[fi][val], counter[fj][val]
            # 兩個小集團合併前，fi 和 fj 要走到「它們的山頭val」的路有 ci cj 條（也就是「高度達val」的山頭： ci 個山頭、cj個山頭）
            ans += ci * cj  # 經過這條「兵家必經之路」edge i 和 j，兩邊的合格山頭 ci, cj 相乘後，便是題目要的 good paths
            f[fj] = fi  # 將 fj 的主人，設成 fi
            counter[fi] = Counter({val: ci+cj})  # 從 node fi 到 最大值是 val 的山頭的 path 有幾條
        return ans

