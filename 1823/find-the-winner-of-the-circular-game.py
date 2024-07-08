# LeetCode 1823. Find the Winner of the Circular Game
# n個人（編號1...n ）繞著圓順時針坐著。
# 現在玩遊戲，從1開始，順時針數第k個人，離開。再繼續數，直到剩1個人。
# 模擬的迴圈，就跑n-1次即可刪到剩1人。
class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        queue = deque() # 利用 double end queue 來實作
        for i in range(1,n+1):
            queue.append(i)  # 先把全部人，都加入queue裡
        for r in range(n-1):  # 要刪除 n-1 人，模擬過程
            for i in range(k-1):  # 數前面k-1人
                queue.append(queue.popleft()) # 拔出來，再塞回去
            queue.popleft()  # 最後這個人，就拔掉
        return queue.pop()  # 剩下的最後1人

