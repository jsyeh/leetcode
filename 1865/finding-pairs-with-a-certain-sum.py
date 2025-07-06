# LeetCode 1865. Finding Pairs With a Certain Sum
# 先給 nums1, nums2。add(index, val) 將 nums2[index] += val 
# 再實作 count(tot) 計算有幾組 (i,j) 使得 num1[i]+num2[j]==tot 
# 因 nums2 很多，需有效率的找 
class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.counter = Counter(nums2)  # 利用 Counter/Hash 快速找
        self.nums1 = nums1
        self.nums2 = nums2

    def add(self, index: int, val: int) -> None:
        self.counter[self.nums2[index]] -= 1  # 舊數 -1
        self.nums2[index] += val  # 修改數值
        self.counter[self.nums2[index]] += 1  # 新數 +1

    def count(self, tot: int) -> int:
        ans = 0
        for num1 in self.nums1:  # 迴圈以數量比較少的 nums1 為主
            # num1 + num2 = tot， 所以去 nums2 找 tot - num1 有幾個
            ans += self.counter[tot - num1]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)
