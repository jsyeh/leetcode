# LeetCode 2211. Count Collisions on a Road
# n 台車「在一條直線上」L往左、R往右、S停止。面對面「對撞」算2次 ans+=2
# 撞到S停止的算1次 ans+=1 。撞了之後，狀態就會變S停止。問 ans 是多少
# 反過來說，「能順利往右離開、往左離開的車」不會撞到，其他在動的都會撞到
class Solution:
    def countCollisions(self, directions: str) -> int:
        N = len(directions)
        counter = Counter(directions)  # 統記每台車的方向
        safe = 0  # 記錄「有幾台車可安全離開」
        for c in directions:
            if c=='L': safe += 1  # 能安全往左離開的車輛
            else: break
        for c in reversed(directions):
            if c=='R': safe += 1  # 能安全往右離開的車量
            else: break
        return counter['R'] + counter['L'] - safe  # 有移動、沒安全，就都會相撞
