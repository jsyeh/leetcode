# LeetCode 3477. Fruits Into Baskets II
# fruits[i] 有第 i 種水果的數量，baskets[j] 是籃子 j 能裝的水果數量
# 每個籃子只放一種水果，依序將每種水果從左到右「找夠大的籃子」放，有幾種水果沒辦法放？
class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        ans = 0  # 有幾種水果找不到籃子、「沒辦法放」？
        for fruit in fruits:  # 依序處理每種水果
            for j in range(len(baskets)):  # 左到右「找夠大的籃子」
                if baskets[j] >= fruit:  # 籃子夠大
                    baskets[j] = 0  # 標註這個之後不能再放水果了
                    break  # 這種水果不用再找籃子了, 離開
            else:  # 小心，這行是 Python for 迴圈(沒break時)對應的 else
                ans += 1  # 很遺憾、沒找到對應的籃子「沒辦法放」記錄下來
        return ans  # 最後剩幾個籃子「沒辦法放」
