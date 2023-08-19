# 這題真的好難，看不懂題目，是第1個難。不知道怎麼解，是第2個難。
# 想看別人的解法卻看不懂，是第3個難。
# 後來發現大家的程式都類似，可能很多人還是不會解，所以用抄的。
# 1. 要如何找出 MST minimal spanning tree? 先把小的edge逐一加上
# 2. 我參考 blackskygg 的解說。先把 origin_mst 算出來，即MST的值
# 3. 暴力法:某edge移除，做出MST比較差，那找到重點edge（關鍵的邊）
# 4. 半重點edge: MST 優先加入「半重點」edge後，得到一樣的 MST值
# 5. 在進行 MST 時，需要用到 UnionFind 技巧，也就是 你是哪一國的？
#    union(a,b) 合成同一國，find(a) 知道是哪一國（函式呼叫函式）
# 6. buildMST() 函式，動手腳加參數，讓它能做不同的行為 
# 6.0. buildMST(nodeN, edges, block, must)
# 6.1. block 不要用的 edge, 可用來找出 critical edge
# 6.2. must 一定要用的 edge, 可用來找出 pseudo-criticla edge
# 6.3. 找標準 MST答案時，min = buildMST(nodeN, edges, -1, -1)
# 6.4. 要找critical edge 要避開某edge i 來測試，值變大
#      if minMST < buildMST(nodeN, edges, i, -1)
# 6.5. 要找 pseudo-critical edge 就硬加某 edge i 來測試，值同
#      if minMST == buildMST(nodeN, edges, -1, i)

class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        # 先把 edges 排序，但答案又需要原本 index 所以先加 index
        for i in range(len(edges)):
            edges[i].append(i) # 每個 edges[i][3] 是編號i
        # 再照 edges[i][2] 也就是 edge i 的 weight 值排序
        edges.sort(key=lambda x: x[2]) # 以 weight 排序

        # 把標準 MST 建出來，得到它的 value （參數：避開or必要）
        def buildMST(block: int, must: int)->int:
        # 可用上一層的 n 及 edges (要事先照 [2] 排序)，就省略參數
            # print("buildMST:", block, must)

            lead = list(range(n)) # UnionFind labels，都不同
            def findLead(a: int)->int:
                if lead[a] == a: # 領袖級人才，自己管自己
                    return a
                else: 
                    return findLead(lead[a]) # 再找下去

            weight = 0 # 還沒加入任何 edge 時，weight為0
            
            if must != -1: # 先把 must 的 edge 加入 MST 裡
                weight += edges[must][2] # 加入 weight
                a, b = edges[must][0], edges[must][1]
                a, b = findLead(a), findLead(b)
                lead[b] = a # leadA當真領袖

            for i in range(len(edges)): 
                # 因edges已排序，會小到大取出
                if i == block: # 要避開的，不要用
                    continue
                edge = edges[i]
                a, b = findLead(edge[0]), findLead(edge[1])
                if a != b: # 不同組
                    weight += edge[2]
                    lead[b] = a # 接起來
            # print("lead:", lead, "weight:", weight)
            for a in range(n):
                if findLead(a) != findLead(0): # 有不同國
                    return inf # 沒救了，無限大 (小心，曾寫錯)
            return weight # 大家都在裡面，把edge加總的值回傳
        
        # 接下來，用 for 迴圈逐測試每個 edge 的重要性
        minMST = buildMST(-1, -1) # 不block, 不must任一edge

        critical = []
        pseudo_critical = []
        for i in range(len(edges)): # 逐一測試
            # print("===edge:", edges[i][3])
            if minMST < buildMST(i, -1): # 少了i就不行
                critical.append(edges[i][3]) # 加入 index
            elif minMST == buildMST(-1, i): # 加入i就剛好
                pseudo_critical.append(edges[i][3]) # 加入index
        return [critical, pseudo_critical]
