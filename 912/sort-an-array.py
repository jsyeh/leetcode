# LeetCode 912. Sort an Array
# 就直接請你將 array 排序，不過有規定「不可以用內建sort()功能」
# 因為有 10^5 個數字，所以2層迴圈一定會超時。要用 n*log(n)的演算法
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        nums.sort()  # 喂！題目說不能用預設的 sort() 耶！ 
        return nums
        
