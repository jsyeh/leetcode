# LeetCode 1331. Rank Transform of an Array
# 想知道 arr[i] 在 arr 裡對應的 rank 排名（小到大）
# 另外，相同的數，rank 要相同。後面再繼續接著排下去（不用避開）
# ex. [10,10,20,1] 要回傳 [2,2,3,1]
# 巧妙使用 sort 做出對照表，再「照著對照表」填寫名次即可
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        data = list(set(arr)) # 去除重覆的數
        data.sort() # 再由小到大排序好
        table = { data[i]:i for i in range(len(data)) } # 分數:名次 對照表

        for i in range(len(arr)): # 想回收 arr 再利用
            arr[i] = table[arr[i]] + 1 # rank 從1開始
        return arr
