# height 有高有低，在兩個高的中間可積水。
# 使用 DP 算出 left_max[i] 表示height[i]這格往左看，最高有多高
# right_max[i] 表示 height[i] 這格往右看，最高有多高
# 積水的量，其實就是「左邊最高」與「右邊最高」以低的為準，能裝的水
class Solution:
    def trap(self, height: List[int]) -> int:
        N = len(height)
        left_max = [0]*N # 表示height[i]這格往左看，最高有多高
        right_max = [0]*N # 表示height[i]這格往右看，最高有多高

        left_max[0] = height[0] # 最左邊那格
        for i in range(1,N): # 其他格，用DP逐格更新
            left_max[i] = max(left_max[i-1], height[i])

        right_max[-1] = height[-1] # 最右邊那格
        for i in range(N-2,-1,-1): # 倒過來的迴圈，用DP逐格更新
            right_max[i] = max(right_max[i+1], height[i])
        
        ans = 0 # 累積答案
        for i in range(N): # 每一個，都可能積水。就水面高度-本身高度
            ans += min(left_max[i], right_max[i])-height[i]
        return ans
