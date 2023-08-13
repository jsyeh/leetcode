# 籃子有 10^5 個，籃子的位置介於1...10^9

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        N = len(position)
        def possible(dist)->bool:
            prev = position[0] # 第一個球放最左邊
            balls = m - 1 # 剩下 m-1 個球
            for i in range(1, N):
                if position[i]-prev >= dist:
                    prev = position[i]
                    balls -= 1
                if balls <= 0:
                    break
            if balls<=0: return True
            else: return False
        position.sort() # 先把座標排序，便知籃子相鄰距離
        # 如果最短距離是left, 可行嗎
        left, right = 1, position[N-1]-position[0]+1
        # 因為最少有2顆球，所以最大的距離，應是最右-最左
        while left<right:
            mid = (left+right) // 2
            if possible(mid): # 可能的話，可加大距離
                left = mid + 1
            else:
                right = mid
        return left - 1
