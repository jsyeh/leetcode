class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        # 這題很簡單，就把答案加總後，排序，取前k個的index即可
        # 我趁機熟悉 enumerate() 迴圈用法 & 陣列取前k項
        sums = [[sum(m), i] for i,m in enumerate(mat)]
        sums.sort()
        ans = [sums[i][1] for i in range(k)]
        return ans
        
