# 這題比 1991. Find the Middle Index in Array （只分2段）稍難
# 數字也變多了，需要用 prefix running sum 來加速
class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        total = sum(arr) # 先有全部加起來的值
        if total%3 != 0: return False # 不是3的倍數，不能分3分
        part1 = total // 3
        part2 = part1 * 2

        prefixSum = set() # 用 set 來存值
        nowSum = 0
        #for now in arr: # 每個數巡一輪
        for i in range(len(arr)-1): # 最後1個避開，才能有3段
            nowSum += arr[i]
            if nowSum == part2 and part1 in prefixSum:
                return True # 剛好三分天下
            prefixSum.add(nowSum)
        return False
# case 70/72: [1,-1,1,-1] 要分成3段，所以part2 要避開最後1筆
