# 「相鄰k個數」裡，有幾個「不同的數」
# 所以 1,2,3,2,2,1,3
#     ^^^^^
#       ^^^^^
#        .....^^^^^ 要 return N-k+1 個答案
# 因數字超多，不能用暴力法
class Solution:
    def distinctNumbers(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums[:k]) # 先取前k個數
        ans = [len(counter)]
        for i in range(len(nums)-k):
            counter[nums[i]] -= 1
            counter[nums[i+k]] += 1
            # counter += Counter() # 這行很沒有效率
            if counter[nums[i]]==0: del counter[nums[i]]
            ans.append(len(counter))
        return ans
# case 59/69: 有大量的數字, k=21123, 這時不能用 counter += Counter()更新
# 改用 if counter[nums[i]]==0: del counter[nums[i]] 即可
