# 想知道 arr[i] 在 arr 裡對應的 rank 排名
# 另外，相同的數，rank 應該要相同。後面再繼續接著排下去
# arr 有 10^5 很多數，所以不能用暴力法。要巧妙使用 sort
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        data = list(set(arr)) # 去除重覆的數
        data.sort() # 再由小到大排序好
        table = { data[i]:i for i in range(len(data)) }

        # 想回收 arr 再利用
        for i in range(len(arr)):
            arr[i] = table[arr[i]] + 1 # rank 從1開始
        return arr
