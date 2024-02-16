# 刪掉 k 個數後，有幾個 unique 的整數？
# 可以先用 counter 統計，再將次數 sort() 再看能減幾個數
# 因 k <= 10^5 所以暴力法應可。(使用 binary search 可能更快)
class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr) # 統計出現次數
        H = []
        for num in counter:
            H.append(counter[num]) # 先轉換成 Histogram
        H.sort() # 再排序
        print(H)
        # 接下來暴力檢測「k能刪掉幾組數字」
        for i in range(len(H)):
            if k >= H[i]: # k 還夠減
                k -= H[i] # 就由小到大，全減光
            else: # 可以回傳答案了
                return len(H) - i
        return 0 # 減光光了，只好 return 0
# case 3/43: [2,4,1,8,3,5,1,3] k=3
