# LeetCode 841. Keys and Rooms
# n 個房間，0沒鎖。rooms[i] 可得到對應的鑰匙，問是否能全部打開房間
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        queue = deque([0])
        visited = set([0])
        while queue:
            now = queue.popleft()
            for k in rooms[now]:
                if k not in visited:
                    visited.add(k)
                    queue.append(k)
        return len(visited)==len(rooms)
