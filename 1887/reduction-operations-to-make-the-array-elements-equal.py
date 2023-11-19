# 一系列的操作：找到最大的，降低到次小的（一定要嚴格變小，不能不動）
# 問要做幾步後，（會降成）大家都一樣小。
# 可用 Excel 的長條圖來想，像樓梯一樣「步步高昇」
# 累積（橫條的空格長度）有幾條後，便能反過來扣掉，知道要降幾格
# 以 11223 為例
#    xxxx3   step會存4 height抬升到2 step現在是[2,4]
#    xx223  step會存2 height抬升到1
#    11223 step=[]  height初始值0
# 所以答案是 height*len(nums)-sum(step) 推導的公式
# 2*5 - sum([2,4]) = 2*5 - 6 = 4
class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort() # 從小到大排好
        # 接下來，看有幾個不同的數字，便是要裁小的步驟
        step = [] # 用來存橫的長條 xx, xxxx 之類的數
        height = 0 # 高度從0開始抬升

        # 迴圈中，i表示往右走到第幾格
        for i in range(1,len(nums)): # 要和前一項比
            if nums[i-1] != nums[i]: # 不同，有抬升
                step.append(i) # i表示往右第幾格、抬升的橫條長
                height += 1 # 增加一格的高度
        # print(step) # Debug觀察用
        return height*len(nums)-sum(step) # 前面推導的公式
