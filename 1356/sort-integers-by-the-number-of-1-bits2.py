# LeetCode 1356. Sort Integers by The Number of 1 Bits
# 排序的規則：先看「二進位」有幾個1，少到多排。相同時，再照x值來排
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        def helper(x):  # 所以寫個 helper()函式，照規則回傳值
            return (bin(x).count('1'), x)
        return sorted(arr, key=helper)  # 再照著排序即可

