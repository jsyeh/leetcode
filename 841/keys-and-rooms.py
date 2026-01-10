# LeetCode 841. Keys and Rooms
# n 個房間，0沒鎖。rooms[i] 可得到對應的鑰匙，問是否能全部打開房間
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        key = set()
        def dfs(i):
            visited.add(i)
            for k in rooms[i]:
                if k not in key and k not in visited:
                    dfs(k)
                    key.add(k)
        dfs(0)
        return len(visited)==len(rooms)
