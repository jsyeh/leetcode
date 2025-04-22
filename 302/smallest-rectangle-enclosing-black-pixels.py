# LeetCode 302. Smallest Rectangle Enclosing Black Pixels
# image 陣列裡，(x,y)座標是黑的。黑的連成一大塊，問 bounding box 有多大
class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        M, N = len(image), len(image[0])
        visited = set((x,y))  # 走過的不能再走
        queue = deque([(x,y)])
        maxX = minX = x
        maxY = minY = y
        while queue:  # 利用 queue 資料結構，進行 BFS
            x, y = queue.popleft()
            for i,j in (x+1,y),(x-1,y),(x,y+1),(x,y-1):
                if i<0 or j<0 or i>=M or j>=N: continue  # 不能超過範圍
                if image[i][j] == '1' and (i,j) not in visited:  # 沒去過的黑色pixel
                    visited.add((i,j))
                    queue.append((i,j))
                    maxX = max(maxX, i)  # 更新4個方向的邊界
                    maxY = max(maxY, j)
                    minX = min(minX, i)
                    minY = min(minY, j)
        return (maxX-minX+1) * (maxY-minY+1)  # 算出面積
