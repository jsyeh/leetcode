# k-distant index i 表示 nums[i] 去找 距離<=k的數j，且nums[j] == key
# 也就是 nums[i] 距離k以內的鄰居裡，有個數是 key
# 把這些i存在陣列裡，排序後回傳。
# 只有 1000個數，用暴力法即可
class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        ans = []
        N = len(nums)
        for i in range(N):
            for j in range(max(0,i-k), min(N,i+k+1)):
                if nums[j]==key: # 找到j,所以i是
                    ans.append(i)
                    break # 結束這一輪
        ans.sort()
        return ans
