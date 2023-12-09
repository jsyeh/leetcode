# 為了節能減碳，大家坐車要共乘。不過車的座位seat有上限。
# 大家都要到0，能共乘，最少要多少的燃油。
# 其實 BFS/DFS 就可解了
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        N = len(roads) + 1 # 路 = 城市-1
        path = defaultdict(list) # 路可以走到哪裡
        for a,b in roads: # 路的兩端a,b
            path[a].append(b) # 互相可到對方城市
            path[b].append(a) # 互相可到對方城市

        self.ans = 0 # 全部耗的油量
        visited = [False]*N # 每個城市走過就不再回頭
        
        # 接下來 DFS, 反過來想，從中心點0出發，往外走，return時再收回來
        def visiting(src:int)->int:
            user = 0
            visited[src] = True
            for dst in path[src]: # 從src能到的全部dst
                if not visited[dst]: # 走過的不能再走
                    now = visiting(dst) # 從dst這條路「過來幾個人」
                    self.ans += (now+seats-1) // seats 
                    # 從dst到src到達本節點的油耗，無條件進位的技巧
                    user += now # 本節點的人數增加
            return user + 1 # 加本人
        
        visiting(0) # 現在從中心點開始出發，函式回傳時，會逐一累積油耗
        return self.ans # 全部的油耗
