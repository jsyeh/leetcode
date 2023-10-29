# 這題的題目很搞笑，可憐的小豬豬，要喝毒藥
# 有點像2進位的想法，不過不是2進位，是s進位
# 註：我有看 Discuss 有人講 60/15＝4卻有5個s狀態，然後懂了!
class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        s = (minutesToTest//minutesToDie) + 1 
        # 每隻豬，可以處理的 possible states 有這麼多種
        # ex. 60/15 是 4, 代表時間可餵藥4次，有5種狀態
        # 結果：第1次死、第2次才死、第3次才死，第4次才死，都沒死
        #for p in range(1,1001): # 不可從1開始，因可能0隻豬
        for p in range(1001): # 要幾隻豬呢？
            # 就 s^p>=buckets 就夠了，p便是答案
            if s**p>=buckets:
                return p
# case 17/18: 1 結果只要0隻豬就可以了
