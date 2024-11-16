# LeetCode 3254. Find the Power of K-Size Subarrays I
# 陣列power：如果「陣列小到大、間隔差1」就挑最大那個，不然就-1
# 請把長度為k的subarray的「陣列power」都算出來
class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        # 總長就500個，暴力兩層for迴圈，就算完了
        ans = []
        for i in range(len(nums)-k+1):  # 開始點
            bad = 0
            for j in range(k-1):  # k個數，有k-1個間格
                if nums[i+j] +1 != nums[i+j+1]:  # 不是剛好差1
                    bad = 1  # 失敗
            if bad==1: ans.append(-1)  # 沒照順序、失敗，放 -1
            else: ans.append(nums[i+k-1])  # 最右邊的數（最大）
        return ans

