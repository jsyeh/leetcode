# LeetCode 904. Fruit Into Baskets
# 只有兩個籃子，可採2種水果，要連續採收，籃子同種水果可裝很多
# 陣列很長，不能用暴力法去算。可試試 sliding window 毛毛蟲的作法
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0
        counter = Counter()  # 毛毛蟲「身體裡」的數目
        tail = 0  # 毛毛蟲的尾巴
        for head in range(len(fruits)):
            counter[fruits[head]] += 1  # 多一個頭
            while len(counter) > 2:  # 如果有2種以上水果，那尾巴要「右縮」哦！
                counter[fruits[tail]] -= 1  # 左邊尾巴吐掉1格
                if counter[fruits[tail]]==0:  # 這種水果吐光光了
                    del counter[fruits[tail]]  # 體內就少1種水果
                tail += 1  # 尾巴右移1格
            ans = max(ans, head - tail + 1)
        return ans              
