# LeetCode 1579. Remove Max Number of Edges to Keep Graph Fully Traversable
# edge 分3種 type1:只有Alice能走 type2:只有Bob能走 type3:大家都能走
# 問「最多能刪掉幾個edges」都能讓 Graph 裡「每個點」都能互連，也就是 Alice 和 Bob 都能在Graph裡任意走
# 如果題目是「普通」雙向的edge可能會比較簡單。但分成3種「有人能走、有人不能走」，就變複雜了。
# 我偷參考 Solutions 裡 Lee215 的解法：「先處理type3」，再處理「type1」與「type2」，利用 Union Find 來解
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        # Union & Find 的方法，利用「陣列」來標示「組長」是誰
        # find(i) 會在「陣列中」找到「i在的組」的組長。union(i,j) 則能把 「i的組」 和 「j的組」 合併/相連起，並標示「新的組長」
        leader = [i for i in range(n+1)] # 一開始，每人獨立一組，自己就是組長，因題目 1-index 所以陣列要大一點 n+1 格
        def find(i): # 利用「函式呼叫函式」，去探究組長是誰，並更新陣列
            if i==leader[i]: return i # 終止條件：自己就是組長，很好啊！
            leader[i] = find(leader[i])  # 函式呼叫函式，去探究組長是誰，並更新陣列
            return leader[i]
        def union(i, j):  # 可將兩個不同群的node i,j合在一起
            i, j = find(i), find(j)  # 找到2組的組長
            if i==j: return 0  # 兩組組長是同一人，太好了，「不用任何更動」
            leader[i] = j  # 兩組的組長不同人的話，把i併入j組
            return 1  # 「有做1次更動」
        edgeAns, edgeAlice, edgeBob = 0, 0, 0 # edgeAns: 可刪的edge數，edgeBob: 最後Bob能走的edge數
        for t, i, j in edges:  # 第一次逐一處理，只處理type3
            if t==3:  # 如果是 A B 都能走的路，很好，優先用它
                if union(i,j):  # 若有做1次更新，即如果i,j不是同一國，就先合成同一國
                    edgeAlice += 1  # Alice 和 Bob 都多了一個邊能走
                    edgeBob += 1
                else:  # 本來就是同一國的話，此 edge 是無用的，可刪
                    edgeAns += 1
        leader1, leader2 = leader[:], leader[:] # 複製陣列，分別只處理 type1 與 type2
        leader = leader1  # 現在 Union & Find 針對 leader1 處理
        for t, i, j in edges:  # 第二次逐一處理 type1 （只能由Alice走的edge）
            if t==1:  # 只更新 leader 也就是 leader1 與 edgeAlice
                if union(i,j): # 有做1次更新
                    edgeAlice += 1
                else:
                    edgeAns += 1 # 無用的 edge
        leader = leader2  # 現在 Union & Find 針對 leader2 處理
        for t, i, j in edges:  # 第三次逐一處理 type1 （只能由Bob走的edge）
            if t==2:
                if union(i,j):
                    edgeBob += 1
                else:
                    edgeAns += 1
        if edgeAlice == edgeBob == n-1:  return edgeAns  # 都是最精簡的 n-1 edge
        else: return -1  # 完全無法走到
