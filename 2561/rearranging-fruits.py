# LeetCode 2561. Rearranging Fruits
# 2個水果籃 basket1 和 basket2 有裡面每個水果的價錢。希望兩籃裡的水果相同。
# 每次交換2水果需代價 min(basket1[i], basket2[j])，最少需要付出多少代價？
# ex. basket1 = [1,1], basket2 = [2,2] 交換後，變 [1,2] vs. [2,1] 可以！
class Solution:
    def minCost(self, basket1: List[int], basket2: List[int]) -> int:
        smallest = min(min(basket1), min(basket2))  # Hint 1: 最小值（交換2次後回原位）
        counter1 = Counter(basket1)  # Hint 1: 統計水果出現次數
        counter2 = Counter(basket2)
        counter = counter1 + counter2  # 全部的水果總數
        for c in counter:  # Hint 2: 針對每一種水果的總數，逐一檢查
            if counter[c] % 2 != 0: return -1  # 不是偶數，就無法平均分配
            counter[c] = counter[c] // 2  # 平分一半的數量
        waiting1, waiting2 = [], []  # Hint 3: 有哪些水果需要交換，小到大排好
        for c in counter:
            if counter1[c] > counter[c]:  # 超過「均分的平均數量」
                waiting1 += [c] * (counter1[c]-counter[c])  # basket1 需移走哪些
            if counter2[c] > counter[c]:  # 超過「均分的平均數量」
                waiting2 += [c] * (counter2[c]-counter[c])  # basket2 需移走哪些
        waiting = sorted(waiting1 + waiting2)  # 待移動的水果，小到大排好（小的價錢重要）
        ans = 0
        for i in range(len(waiting)//2):  # 全部要移動的，只看「最小的那一半」，因「以小計價」
            ans += min(smallest *2, waiting[i])  # 移動法：可用「最小值」動2次 or 小的（會兌掉大的）
        return ans
