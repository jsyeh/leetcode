# mat 的每個 row 都有的「最小」數
# 還是可以用 set() 來做
class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        M = len(mat)
        sets = [set(mat[i]) for i in range(M)]
        union = sets[0]
        for i in range(1,M):
            union = union & sets[i] # 一直取「交集」
        
        if len(union)==0: return -1
        return min(union) # 找到最小的數
# case 9/13: 一堆數字，但交集是空集合
