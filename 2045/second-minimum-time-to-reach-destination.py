# LeetCode 2045. Second Minimum Time to Reach Destination
# 頂點1...頂點n，存在一堆 edges，每走1段，耗時time分鐘，但只能在綠燈走
# 綠燈、紅燈、綠燈、紅燈，各佔 change 分鐘。從 頂點1 走到 頂點n，第2快，要多久？
class Solution:
    def secondMinimum(self, n: int, edges: List[List[int]], time: int, change: int) -> int:
        graph = defaultdict(list)
        for a,b in edges:  # 先把 edges 裡 a b 相連，轉成能快速找到的資料結構
            graph[a].append(b) # 也就是與a相連的全部頂點，都在 graph[a]裡
            graph[b].append(a) # 與b相連的，都在 graph[b]裡
        ans = [[] for _ in range(n+1)] # ans[i] 「到達」頂點i 的2個可能時間（目前還沒有）
        heap = [[0,1]] # 在第0分鐘，到達頂點1

        while heap: # 利用 Priority Queue 來做，照著「到達」時間，依序處理
            t, a = heappop(heap)  # 在 t 時間，到達頂點a
            if a==n and len(ans[a])==2:  # 終止條件：到達頂點n，且有2個可能的時間
                return ans[n][1] # 後面的時間，就是第2快的時間

            for b in graph[a]:  # 接下來，從頂點a出發，到相鄰的頂點b
                if t % (2*change) < change: # 運氣不錯，剛好是綠燈
                    t2 = t + time # 到達 b 的時間，直接相加就好，不用等紅綠燈
                else: # 不幸遇到紅燈，要等到變綠燈
                    t2 = (t//(2*change)+1)*2*change + time # 等到變綠燈時，再+time就是 到達 b 的時間
                # 有兩種情況有進展：還沒有到達過b 或 (目前到達b的時間只有最短時間1個，且與t2不同，能更新)
                if len(ans[b])==0 or (len(ans[b])==1 and ans[b][0]!=t2):
                    ans[b].append(t2)  # 把新的時間t2 加到 ans[b] 裡
                    heappush(heap, (t2,b))  # 把新的時間t2 加到 heap 裡

