# LeetCode 632. Smallest Range Covering Elements from K Lists
# 有 k 條「從小排到大」的 lists，找個範圍，讓k條都有人被包含住
# 討論區有人說：「把k條merge」後，再用sliding window (毛毛蟲) 找範圍，我照這個技巧來寫
class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        k = len(nums)  # 有 k 條 lists
        heap = []  # 可找到 k 條lists 每一條的「目前最小的數」的最小的數        
        M = nums[0][0]  # heap裡的最大值
        for i in range(k):  # 每條 list 都把最前面的頭 nums[i][0] 放到 heap裡
            heappush(heap, (nums[i][0],i))  # heap 裡，放「每條的最小的數」及「對應的index i」
            M = max(M, nums[i][0])  # 持續更新 heap裡的最大值
        ii = [1]*k  # 第i條 list，下次要處理的 index ii[i]（每條的 index 0剛用掉，現在變1）
        ansLen = inf  # 最誇張的長度 inf 無限大，之後會更新
        ans = [heap[0][0], inf] # 用來放「答案」的左右範圍：左邊是 heap最小那坨的數，右邊是 inf無限大
        while len(heap)>0:  # 只要 heap 還有值，就繼續處理
            m, i = heappop(heap)  # 取出目前最小的數 m 及對應的 list index i（毛毛蟲左邊的尾巴吐出）
            if M-m < ansLen:  # （目前 heap 裡最大值，最小值）若範圍更短，就更新
                ansLen = M-m  # 更新長度（更短）
                ans = [m, M]  # 同時得到新的範圍
            if ii[i]<len(nums[i]):  # 因在heap中取出 nums[i] 代表的數，若它還有數，就遞補進 heap （這樣就保證「每串都有1位代表」）
                M = max(M, nums[i][ii[i]])  # 接下來 heap 裡的最大值
                heappush(heap, (nums[i][ii[i]],i))  # 順手將 nums[i] 的下個數放入 heap（毛毛蟲右邊的嘴巴吃入）
                ii[i] += 1  # 下次要處理的 index 位置右移1格
            else: return ans
        return ans
