# LeetCode 1570. Dot Product of Two Sparse Vectors
# 兩個向量的內積
class SparseVector:
    def __init__(self, nums: List[int]):
        self.v = {}  # 只記錄 non-zero 項
        for i in range(len(nums)):
            if nums[i] != 0:  # 遇到「非0項」加入  裡
                self.v[i] = nums[i]

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        for i in self.v:  # 存在的項，才去乘
            if i in vec.v:
                ans += self.v[i] * vec.v[i]
        return ans
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)
