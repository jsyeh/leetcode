# 3位數以上 挑「等差級數」，共幾組？ 以 7,7,7,7,7 為例，分析如下
# 77777  77777 
# ijk    hijk
# ij k   hij k
# ij  k  hi jk
# i jk   h ijk
# i j k   hijk 以上5筆，可解決4位數
# i  jk
#  ijk   hijkl 這1筆，可解決5位數，故共10+5+1=16筆
#  ij k
#  i jk
#   ijk 以上10筆，可解決3位數
# 可用 動態規劃 DP解 table[i][diff] 但diff範圍太大，右邊要改用dict
# 字典裡，diff差多少：對應「有幾個可能」
# 因數字僅1000個，所以for迴圈裡，再用for往前巡一輪，是可以的。
# 很有緣份，我的想法，和 hiepit 的解法思緒很像。
class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        N = len(nums)
        table = [defaultdict(int) for i in range(N)] 
        # 左邊[i],右邊是字典 defaultdict(int) 對應 [i][diff] 有幾個可能
        # table[i] 對應 nums[i] 之前有幾種可能的等差級數(兩項以上)
        # ex. table[i][0] 表示 nums[i] 前面相距 0 的數列有幾種可能
        ans = 0
        for i in range(N): # 現在處理第i個數
            for p in range(i): # 前個數是第p個數
                diff = nums[i]-nums[p] # 等差的「差」，要問
                table[i][diff] += 1 # 距離 diff 的多1筆
                if diff in table[p]: # 若這個差，剛好在p也有過(2項以上)
                    count = table[p][diff] # 可以接續下去的數量
                    table[i][diff] += count # 前面第p個也差diff
                    # 所以前面的值也拿來增加可能性的次數
                    ans += count # 更前面、p、i 湊3個以上，count可加入
                    # table[p][diff] 前面兩項以上 count，加i就3項
        return ans
