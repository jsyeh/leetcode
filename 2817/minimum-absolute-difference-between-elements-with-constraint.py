# abs(i-j)>=x and abs(nums[i]-nums[j]) 最小
# 也就是距離夠遠的兩數「越接近越好」
# 10^5 不能用暴力法，又「距離夠遠」所以先不能排序
# 看 Solutions 裡 vortrubac 的解釋，用一層迴圈即可。
# 保持距離 x 的迴圈走法，配合 set 的 upper_bound來完成。
# 我本來想用兩個 heap (priority queue) 來查最大、最小值
# 但我錯了。不是要找最大、最小值。是要找「與nums[i]最接近的值」
# 所以需要 binary search 來完成。

# 下面會用到我還不熟的 SortedSet 配合 bisect_bisect_left()
from sortedcontainers import SortedSet # 這行不熟
class Solution:
    def minAbsoluteDifference(self, nums: List[int], x: int) -> int:
        s = SortedSet()
        N = len(nums)
        ans = inf
        for i in range(x, N): # nums[0]..nums[x] 距離x
            s.add(nums[i-x]) # nums[i] 的前面 x 格
            ii = bisect.bisect_left(s, nums[i]) # 看最近在哪裡
            # s[ii] 及 s[ii+1] 分別在 nums[i] 的左右側
            # 所以只要沒撞到邊界，就都要量測「最小距離」
            if ii>0: ans = min(ans, nums[i]-s[ii-1])
            if ii<len(s): ans = min(ans, s[ii]-nums[i])
        return ans
