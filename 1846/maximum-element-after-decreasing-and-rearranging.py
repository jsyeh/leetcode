# 這個題目有點看不懂，而且看了它的Input/Output後，心中有些疑問
# 為什麼 1 100 1000 最大值會是3呢？變成 1 1 1 不好嗎？
# 後來看了 Editorial 後，發現「數字變小」有個限制，要慢慢變大
# 後來把題目翻譯成中文後，了解它想知道「最大的數」
# 「數字只能變小」且「相鄰的數只能差0或1，就像個鏈條，限制抬昇速度
# 所以想要找到最大的數的話，就要努力的+1
class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort() # 從小到大排好
        N = len(arr)
        arr[0] = 1 # 題目規定第1個數字要是1
        for i in range(1, N): # 逐一檢查arr[i-1] arr[i]
            if arr[i] > arr[i-1] + 1: # 抬昇太多，要降
                arr[i] = arr[i-1] + 1 # 只能抬昇 +1
        
        return arr[-1] # 最後的數字，就是最大的數字
        
