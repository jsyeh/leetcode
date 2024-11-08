# LeetCode 1829. Maximum XOR for Each Query
# nums 從小到大排好，把全部數字 XOR 後，再 XOR k 讓它最大
# 再把最後的數刪掉，再重覆做，並把這些 k 變成 list 回傳
# 其實 XOR 的性質很有趣，要最大，就把是0的bits都變設1即可，剛好就是 allOne XOR 現在的數。
# 且要加速，就反過來，nums[0] 1個數字開始，再XOR累積「越來越多的數字」即可
class Solution:
    def getMaximumXor(self, nums: List[int], maximumBit: int) -> List[int]:
        allOne = (1 << maximumBit) - 1  # 可做出一堆1
        ans = []
        now = 0  # 用來累積「一堆數XOR的結果」從0個，慢慢增加
        for num in nums:  # 「慢慢增加」
            now ^= num  # 多增加1個數 XOR 起來
            ans.append(allOne ^ now)  # 答案k就是 allOne XOR now
        return ans[::-1]  # 答案再「反過來」，就是「全部」再「慢慢變少」的版本
        
