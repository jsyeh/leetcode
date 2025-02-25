# LeetCode 1524. Number of Sub-arrays With Odd Sum
# arr 能挑選出幾種（連續的）subarray，加起來是odd奇數
# 這題好難，一開始我用函式呼叫函式來解，但寫得有點複雜，而且程式好像有錯。
# 後來發現 Vlad 的 Solution 好簡單，比我的程式漂亮，就決定改用這個解法。
class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        ans = 0  # 迴圈前面，答案是 0，開始累積答案
        odd = 0  # 重要技巧：處理到前 i 位時，「到第i位為止」有幾種加法「加起來是奇數」
        MOD = 10**9+7  # 因答案有「太多種」可能，題目要取餘數，
        for i in range(len(arr)):  # 迴圈最多要跑 10^5次，所以ans可能太大
            if arr[i]%2==1:  # arr[i]可能是偶數（和前一項相同）可能是奇數（風雲變色）
                odd = (i-odd) + 1  # 風雲變色時，之前的「偶數和」i-odd種，偶數和+奇數=奇數
                # 所以就修改、變動了「奇數和」有幾種（的數量）
            ans = (ans + odd) % MOD  # 持續加、一直加！記得取餘數，以免 overflow 溢位
        return ans
