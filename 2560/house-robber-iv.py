# LeetCode 2560. House Robber IV
# 題目英文（又是最大、又是最小）不容易讀懂，要花時間理解。看例子就簡單了。
# 搶匪有怪僻：搶房子，但怕鄰居警覺，不搶鄰居。若搶k個房子，有很多種挑法
# 只準備一個包包，每次搶房子只用這個包包。不想要帶太大的包包，夠大就好。
# 搶匪又很懶，不想搶太多錢，只想準備最小的包包（容量c），剛好夠裝k個不相鄰房子的錢
class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
        def possible(c):  # 想知道包包的容量 c 是否可行
            # 模擬搶匪「容量c」的包包，巡一輪，看能不能挑到k個房子搶
            house = 0  # 搶了幾間房子
            mark = -1  # 記一下，下次「不能搶哪一間」
            for i,num in enumerate(nums):  # 巡一輪
                if mark!=i and num <= c:  # 包包夠裝這間的錢，才搶（真奇怪）
                    house += 1
                    mark = i+1  # 記一下，下次不能搶它的鄰居（下一間）
                    if house>=k: return True  # 房子搶夠多了，成功
            return False  # 包包太小、不夠搶，失敗
        return bisect_left(range(max(nums)+1), True, key=possible)
        # 好厲害的 Binary Search，像「猜數字」一樣，快速找到答案
