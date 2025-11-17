# LeetCode 1437. Check If All 1's Are at Least Length K Places Away
# 想確認 nums 裡的 1「彼此距離都很遠」至少隔k個0
class Solution:
    def kLengthApart(self, nums: List[int], k: int) -> bool:
        zeros = k  # 先假裝隔 k 個，方便「第1個1」可直接成功
        for num in nums:
            if num==1:  # 遇到1，要檢查「前面0夠不夠」
                if zeros < k:  # 之前累積的0不夠
                    return False  # 距離不夠，就失敗
                zeros = 0  # 重新「歸零」
            else:  # 遇到 0
                zeros += 1  # 又多1個0，真好
        return True  # 全部走完、平安、沒出錯，成功
