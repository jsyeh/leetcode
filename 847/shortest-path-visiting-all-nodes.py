# https://leetcode.com/problems/shortest-path-visiting-all-nodes/solutions/135686/java-dp-solution/ 
# 我在 2023-07-02 用 Java 寫過這題，當天的挑戰題，也有利用 mask 進行 DP 的作法，很親切
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        N = len(graph)
        maskRange = 1 << N # maskRange 是在迴圈裡使用
        maskAll = maskRange - 1 # 如果 N 是 4個點, 0b1111 我用 maskAll 代表
        # 可以用 for i in range(maskAll) 可把 0b0000 ~ 0b1111 都走過一次

        # table[i][mask] 代表:現在要從i出發的最短值，只考慮mask裡的點全部走到
        table = [[math.inf]*maskRange for _ in range(N)] # 設極大值，方便之後替換
        queue = deque() # 我們要使用 append() 及 popleft()

        for i in range(N): # 思考第 i 個 node
            table[i][1<<i] = 0 # 第i個點，經過i可以到的距離，是0步
            queue.append([1<<i, i]) # 上述每一個都可是簡單的出發點

        while len(queue)>0:
            mask, index = queue.popleft() # 現在走到 index，且走過 mask 對應的點
            for next in graph[index]: # index 之後可再走的點，進行BFS
                # 若走到 next ，mask 會變成 nextMask，多了next這個點
                # 將 nextMask 加 next 對應的 bit 成為更完整的 mask
                nextMask = mask | (1<<next) 
                if table[index][mask] + 1 < table[next][nextMask]:
                    # 若經過 index 到達 next 後，會讓對應的 table值更小的話
                    # 若經由 index 走到 next 的距離，比原本 next 記的距離更短，就更新
                    table[next][nextMask] = table[index][mask] + 1
                    queue.append([nextMask, next]) # 再用這個更新其他相關的 mask 的值

        ans = table[0][maskAll]
        for i in range(N): # 想找出最短的距離值
            if table[i][maskAll] < ans:
                ans = table[i][maskAll]
                # 有更短的距離，就用更短的距離
        return ans
        
