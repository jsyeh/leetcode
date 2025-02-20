# LeetCode 1980. Find Unique Binary String
# n 個「長度是n」的「binary字串」裡面由 0 和 1 組成
# 請隨便找個「長度也是n」且沒有在 nums 裡出現的字串
class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        N = len(nums)
        used = set()  # 想要快一點，就把全部的 nums 都轉成 set
        for num in nums:
            used.add( int(num, 2))  # 把「字串」轉成binary的整數
        for i in range(2**N):  # 2的N次方，會試「所有長度是n」的binary字串
            if i not in used:  # 沒有出現過的數，太好了，這就是答案！
                return bin(i)[2:].zfill(N) 
                # 先轉成 0bXXX的二進位字串，再去[2:]取0b後面的數，再用 0 補齊 N 位數
        return ''  # 這行不會執行到，只是寫好玩的（因前面for迴圈一定找到答案）
