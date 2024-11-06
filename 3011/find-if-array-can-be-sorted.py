# LeetCode 3011. Find if Array Can Be Sorted
class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        N = len(nums)
        bits = []  # 要建 set bits 知道裡面有幾個 1 
        for i in range(N):
            ones, now = 0, nums[i]
            while now>0:  # 剝皮法，數一數「有幾個1」
                ones += now%2  # 累積、有幾個1
                now //= 2
            bits.append(ones)  # 記下 nums[i] 有幾個 1
        # Bubble Sort
        notOK = True
        while notOK:
            notOK = False  # 這一輪，還沒有交換
            for i in range(N-1):
                if nums[i] > nums[i+1]: # 大小不對，需要交換
                    if bits[i] != bits[i+1]:  # 1的數量需相同，才能交換。現在卻不相同
                        return False # 抱歉，無法交換。失敗
                    nums[i], nums[i+1] = nums[i+1], nums[i]  # 交換相鄰的數字（搬家）
                    bits[i], bits[i+1] = bits[i+1], bits[i]  # 也交換它們 1 的數目
                    notOK = True  # 有交換，代表還沒有OK
        return True
