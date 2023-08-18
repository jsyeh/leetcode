class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        # 有種直覺的作法，是XOR全部巡過，便會得到答案 O(n)
        # ans = 0
        # for n in nums:
        #     ans ^= n
        # return ans
# 不過題目要求，要O(log n)的時間，所以不能全部巡一次。
# 可以使用 binary search, 查某2相鄰的是否相同。相同就在右半邊、不相同就在左半邊
        N = len(nums)
        if N==1: return nums[0] # 只有1筆資料，答案就是它，就不用binary search了

        left, right = 0, N-1
        while left < right:
            mid = (left+right)//2
            print(left, right, mid)
            if mid%2==0 and nums[mid] == nums[mid+1]: # 左邊正常，答案在右邊
                left = mid + 2
            elif mid%2==1 and nums[mid-1] == nums[mid]: # 左邊正常，答案在右邊
                left = mid + 1
            else: right = mid
        return nums[left]
# case 3/15: [1,1,2] 造成 index超過。所以 right 初始值寫 N-1 看看
