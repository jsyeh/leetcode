# LeetCode 605. Can Place Flowers
# flowerbed 長長的花壇裡很多格子，0是空的、1有種花，相鄰不能同時種花
# 有沒有可能「順利再將 n 盆花放入花壇裡」？
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        B = len(flowerbed)
        for i in range(B):
            if flowerbed[i]!=0: continue  # 已種花，換下一位
            if i>0 and flowerbed[i-1]!=0: continue  # 左邊已種花，換下一位
            if i<B-1 and flowerbed[i+1]!=0: continue  # 右邊已種花，換下一位
            flowerbed[i] = 1  # 這裡有空間可種花，決定「種花」
            n -= 1  # 又種掉一盆花
        return n<=0  # 要種的花全部都種掉，太棒了！
