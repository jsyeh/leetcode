# 想找到 array 裡，有沒有重覆的數字
# 因為數字只會出現「一次」或「兩次」所以可用 dict 來做
class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        happened = {}
        ans = []
        for num in nums:
            if num in happened:
                ans.append(num)
            happened[num] = True
        return ans
