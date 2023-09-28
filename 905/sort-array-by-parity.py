# 要排序，數字很少，所以不會超時。
# 排序的依據：偶數在左邊、奇數在右邊
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # 第一種方法，使用Python的排序，給個key的規則
        nums.sort(key=lambda x : x%2!=0)
        # 上面的意思是，奇數比較大，所以偶數就到前面了
        return nums
        
