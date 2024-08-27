# LeetCode 1514. Path with Maximum Probability
# 資料結構題：graph裡，有n個頂點，有很多edges標示2端點，對應 succProb 成功走到的機率
# 從 start node 走到 end node，找一條「有最大機率成功」的路線。
# 在 graph 裡搜尋路徑的技巧，通常是 DFS (用stack或函式呼叫函式) 或 BFS (用quque)
# 想找到「最大機率」的話，可利用「heap/priority queue」先挑「機率」大的路徑，一旦到終點，就是答案
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        # 先將 edges 及 succProb 轉成「能快速找到」的對照表
        path = defaultdict(list)
        for i, (a,b) in enumerate(edges):
            path[a].append((b,succProb[i]))  # a可到b，成功機率 succProb[i]
            path[b].append((a,succProb[i]))  # a可到b，成功機率 succProb[i]
        # 為了避免「一直重覆繞圈圈」需要「機率更高」需更新時，才會重走
        city_prob = [0]*n  # 每個城市，一開機到的機率都是0 (把node想像成city可能更具體)
        # 再從 start node 出發，想走到 end node
        heap = [(-1, start_node)]  # 因 heap 會會先挑「小的」，所以把機率「變負號」便能先挑大的
        # 下面有很多機率都加「負號」是因為 heap 會先挑「小的」，「負負得正」可還原成正確的機率值
        while heap:  # 只要 heap 還有東西，就有機會找到答案，繼續做
            prob, node = heappop(heap)  # 現在機率最大的位置，對應 prob 及 node
            if node==end_node: return -prob  # 恭喜，走到終點，這時對應的機率「變負號」便是答案
            for node_b, prob2 in path[node]:  # node 可以往哪裡走
                if -prob*prob2 > city_prob[node_b]:  # 若到達node_b的成功機率更高，便能更新
                    heappush(heap, (prob*prob2, node_b))  # 便能加入 heap 繼續走
                    city_prob[node_b] = -prob*prob2  # 更新這個 city node 的對應機率
        return 0
