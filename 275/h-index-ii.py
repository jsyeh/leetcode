# sorted 的陣列 Linear search 可找到 H-index O(N)
# 但題目希望是 O(logN)，所以必須要使用 binary search
class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        left, right = 0, N
        while left<right:
            mid = (left+right)//2
            # 因要大到小，所以把 citations[mid] 改成 citations[N-1-mid]
            if citations[N-1-mid] > mid: # citation>=mid 是它的定義
                left = mid + 1
            else:
                right = mid
        return left
# case 51/83: [0] 只有1個數字
