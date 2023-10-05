# 要找「超過1/3」的全部數字。就像之前 Joma 的影片
# https://www.youtube.com/watch?v=pKO9UjSeLew
# 用 sort 和 hashmap 一定都能解，但時間限制、空間限制下，應該有更帥的解法
# 這題數字不大，使用任一個都不會超過啦。就隨便挑一個來做。
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        N = len(nums)
        table = {}
        ans = set()
        for n in nums:
            if n in table:
                table[n] += 1
            else:
                table[n] = 1
            if table[n]>N/3:
                ans.add(n)
        
        return list(ans)

