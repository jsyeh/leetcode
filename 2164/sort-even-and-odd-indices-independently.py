# 將數字「重排」：奇數位數要漸減、偶數位數要漸增
# 所以「先拆開」各別排序後，再「組回來」
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        N = len(nums)
        oddItems = [nums[i] for i in range(1,N,2)]
        evenItems = [nums[i] for i in range(0,N,2)]
        oddItems.sort(reverse=True) # 反過來排
        evenItems.sort() # 偶數位 正著排 
        ans = []
        for i in range(N): # 再逐一塞入ans
            if i%2==0: ans.append(evenItems[i//2])
            else: ans.append(oddItems[i//2])
        return ans
