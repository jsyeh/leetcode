# 找「有沒有相同的數」，計算他們與「相同數」的距離
# 技巧：逐一更新距離和，相同數「往右移」時，左邊加，右邊減
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        groups = collections.defaultdict(list)
        for i, num in enumerate(nums):
            groups[num].append(i)
        ans = [0] * len(nums)
        for indices in groups.values(): # index
            m = len(indices)
            dist_sum = 0
            for i in range(1,m):
                dist_sum += abs(indices[0]-indices[i])
            ans[indices[0]] = dist_sum
            for i in range(1,m):
                dist_moved = indices[i] - indices[i-1]
                dist_sum += dist_moved * i # 左邊加（遠離）
                dist_sum -= dist_moved * (m-i) # 右邊減（接近）
                ans[indices[i]] = dist_sum
        return ans
