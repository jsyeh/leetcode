# 修課模擬：每門課可能會有「先修課程」，要先修完「先修課程」才能修後面的課。
# 通常會用 topological sort
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        before = [0]*(n+1) # before[i] 表示「課程i」之前，需要先修幾門課,i從1開始
        graph = {i: [] for i in range(1, n+1)} # graph[i]將會存 i之後可修的課程
        for prev,next in relations:
            before[next] += 1
            graph[prev].append(next)
        
        visited = [False]*(n+1) # visited[i] 這個課有修過了嗎, i從1開始
        visitedN = 0
        queue = deque()
        for i in range(1,n+1):
            if before[i] == 0: # 沒有任何先條課程
                queue.append([1,i]) # 這門課可以在第1學期先修
        
        currentSemester = 0
        while len(queue):
            semester, i = queue.popleft()
            currentSemester = semester
            visited[i] = True # 正式修了課程i
            visitedN += 1 # 現在修了幾門課
            # 本課程i 修過後，解鎖它後面的課程 graph[i]
            for next in graph[i]:
                before[next] -= 1 # next 少掉1門先修課
                if before[next]==0: # 如果有幸這門課的先修課程都全部解鎖
                    queue.append([semester+1, next]) # 下學期便能修課程next
        
        if visitedN==n: return currentSemester
        else: return -1 # 無法將全部課程修完

