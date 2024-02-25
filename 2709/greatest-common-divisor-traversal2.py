# 題意：有一堆數字 nums，如果 nums[i], nums[j] 最大公因數>1 就可走到/相連
# 題目問：「數字間能全部走完嗎？」也就是任兩數，都能「走到」
# 因 10^5 個數字太多了，無法「暴力」去試全部的可能，是 Hard 題
# 
# 這題好難啊！我模仿 cpcs 今天的寫法後，成功送出，Python執行5178ms
# 但發現有人耗時更短，Python執行458ms快十倍，程式碼又精簡。
# 我研究理解後，決定用這種方法寫看看。
class Solution:
    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        N = len(nums)
        if N==1: return True # 只有1個數字，一定能「相連」成功
        if 1 in nums: return False # 不幸有1的話，gcd() 就無法>1失敗
        nums.sort(reverse=True) # 數字從大到小排，希望右邊小一點（因右邊會變大）
        # 而且右邊的數會重覆算gcd()很多次，越小越好

        for i in range(N-1): # 左手i
            for j in range(i+1,N): # 右手j
                d = gcd(nums[i],nums[j]) # Python內建math.gcd()
                if d>1: # 題目希望 gcd>1 代表兩數相連 
                    # 若找到可和nums[i]相連的數nums[j]，就交棒給 nums[j]
                    nums[j] *= nums[i] // d # 右邊會變大 ex. 21 14 => 14*21//7 得42
                    # nums[j] 將內含 nums[i]，並除掉共同部分
                    break
            else: # Python for-else語法，整輪巡完，若沒break，就會else
                return False # nums[i] 找不到(能相連的)同伴 nums[j] 就是失敗
        return True # 能全部數字都找到相連的關係/沒有落單的nums[i]，就是成功       
