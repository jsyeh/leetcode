# 要排序，數字很少，所以不會超時。
# 排序的依據：偶數在左邊、奇數在右邊
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # 第二種方法，逐一比對，先放偶數，再放奇數
        ans = []
        for num in nums:
            if num%2==0:
                ans.append(num)
        # 上面先把偶數加到ans裡
        # 下面再把奇數加到ans裡
        for num in nums:
            if num%2==1:
                ans.append(num)
        return ans # 最後把 ans 送出去
        
