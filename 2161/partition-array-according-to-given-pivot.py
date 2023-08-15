# 這題與 86. Partition List 有點像，但 Array 不好插入
class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        N = len(nums)
        bigger = [0]*N # 浪費記憶體，用來存 bigger 的數

        pivotN = 0
        i0, i1 = 0, 0 # nums[i0] vs. bigger[i1]
        for i in range(N):
            if nums[i] == pivot:
                pivotN += 1
            if nums[i] < pivot:
                nums[i0] = nums[i]
                i0 += 1
            if nums[i] > pivot:
                bigger[i1] = nums[i]
                i1 += 1
        # 結束時，把答案依序放進來，也就是補上 pivotN 個 pivot 及 bigger
        for i in range(pivotN):
            nums[i0+i] = pivot
        for i in range(i1):
            nums[i0+pivotN+i] = bigger[i]

        return nums
