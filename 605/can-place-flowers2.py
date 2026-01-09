# LeetCode 605. Can Place Flowers
# flowerbed 長長的花壇裡很多格子，0是空的、1有種花，相鄰不能同時種花
# 有沒有可能「順利再將 n 盆花放入花壇裡」？
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # 照著規則放花即可
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:  # 找到空位
                if (i==0 or flowerbed[i-1]==0) and (i+1==len(flowerbed) or flowerbed[i+1]==0):
                    flowerbed[i] = 1   # 找到位置種花
                    n -= 1
                    if n <= 0: return True  # 順利把花種完，成功
        return n <= 0  # 最後有沒有把花種完呢？
''' 這題我沒考慮到好多 case 值得記下來
[1,0,0,0,0,1]
2
[1,0,1,0,1,0,1]
0
[0,0,1,0,1]
1
'''
