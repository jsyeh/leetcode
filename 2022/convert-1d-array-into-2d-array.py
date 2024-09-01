# LeetCode 2022. Convert 1D Array Into 2D Array
# 把 1D 陣列，轉成 2D 陣列
class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: return [] # 如果長寬大小「不符合」, 要 return []
        # 照著 i,j 的座標，從 original[] 取出值，填入 2D 陣列的答案裡
        return [[original[i*n+j] for j in range(n)] for i in range(m)]
