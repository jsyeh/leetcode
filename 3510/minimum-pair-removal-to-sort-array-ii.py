# LeetCode 3510. Minimum Pair Removal to Sort Array II
# 每次挑「相鄰2數」加起來最小的，幾次後，可小到大排好。數字很多，要設計「資料結構」
class Solution:
    def minimumPairRemoval(self, nums: List[int]) -> int:
        N = len(nums)
        prev = {i:i-1 for i in range(N)}  # 資料結構1：上一筆
        next = {i:i+1 for i in range(N)}  # 資料結構2：下一筆
        deleted = set()  # 資料結構3：nums陣列裡哪些數「已刪除」
        heap = []  # 資料結構4：找「相鄰兩數加起來最小」
        bad = 0  # 技巧：陣列裡，大小「順序不對」的數量
        for i in range(N-1):  # 從左到右巡「相鄰的數」
            heappush(heap, (nums[i]+nums[i+1],i,i+1))  # 建立「資料結構4」
            if nums[i] > nums[i+1]: bad += 1  # 技巧：陣列裡，有幾組「大小順序不對」
        step = 0  # 答案：要做「幾步」後，能讓順序正確
        while bad > 0:  # 只要還有順序不對
            minSum, i, j = heappop(heap)  # 用「資料結構4」吐出最小的相鄰2個數
            if i in deleted or j in deleted or nums[i]+nums[j] != minSum:
                continue  # 已刪除的數 or 已無效的數，就不要用它們、換下一組
            i0, j1 = prev[i], next[j]  # 用「資料結構1、2」找到前一筆、後一筆
            prevBad = (nums[i0]>nums[i] if i0>=0 else 0) + (nums[i]>nums[j]) + (nums[j]>nums[j1] if j1<N else 0)
            nums[i] = minSum  # 要將 nums[i] 和 nums[j] 合併（上面那行prevBad，是合併前「前後i0,i,j,j1」「順序不對」的數量）
            deleted.add(j)  # node j 被刪除，對應 nums[j] 不再使用（下面那行nowBad，是合併後「前後i0,i,j1」「順序不對」的數量）
            nowBad = (nums[i0]>nums[i] if i0>=0 else 0) + (nums[i]>nums[j1] if j1<N else 0)
            bad += nowBad - prevBad  # 更新「順序不對」的數量，也就是「合併前、合併後」的改變量
            prev[j1], next[i] = i, j1  # 更新「資料結構1、2」
            step += 1
            if i0>=0: heappush(heap, (nums[i0]+nums[i], i0, i))  # 更新「資料結構4」i0,i 的部分
            if j1<N: heappush(heap, (nums[i]+nums[j1], i, j1))  # 更新「資料結構4」i,j1 的部分
        return step
