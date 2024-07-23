# LeetCode 1636. Sort Array by Increasing Frequency
# 要統計一下數字出現的次數：次數少的放前面。次數相同時，數字大的放前面
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)  # 可用 Counter() 統計數字出現次數
        # counter2 是個 list, 將「出現頻率」及「數字」放進去
        counter2 = [(freq,num) for num,freq in counter.items()]
        # 因數字不大，想到1個公式，可同時考慮到「頻率」及「數字大小」一起排序
        counter2.sort(key=lambda x:x[0]*200-x[1]) 
        ans = []
        for freq,num in counter2: # 再照著排序後的順序
            ans += [num]*freq  # 把答案（照出現數量）塞入 ans 裡
        return ans

