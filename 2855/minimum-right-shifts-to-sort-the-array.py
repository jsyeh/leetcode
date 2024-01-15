# right shift: 將 nums[i] 移到 nums[ (i+1)%n ]
# 想知道 right shift 要做幾次，才能 sort完成。
# 因為數字實在很少 100 個，所以暴力法就可以成功了
class Solution:
    def minimumRightShifts(self, nums: List[int]) -> int:
        N = len(nums)
        for shift in range(N): # 決定這次的移動的位數
            bad = 0
            for i in range(N-1): # 逐項檢查，看是否排序好
                # 應該要 nums[i] <= nums[i+1]
                # 右位移後，要反過來左位移看原本位置的值
                #print(nums[(i+N-shift)%N], nums[(i+N-shift+1)%N])
                if nums[(i+N-shift)%N] > nums[(i+N-shift+1)%N]:
                    bad = 1 # 但若有任一組沒排好順序
                    print('bad')
                    break # 就失敗
            if bad==0: return shift # 若都沒失敗，便成功
        return -1 # 都沒成功，就 -1
