# LeetCode 860. Lemonade Change 檸檬水攤找零錢
# 每份5元，一堆客人手拿5元、10元、20元鈔，排隊買。
# 能全部成功找零，就true。中間無法找零，就false。用一堆 if 就可以解了！
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        d5, d10, d20 = 0, 0, 0  # 攤商：3種鈔票，一開始都0張
        for bill in bills:  # 顧客手拿鈔票，排隊買涼水
            if bill == 5:  # 錢剛剛好，不用找零
                d5 += 1  # 5元鈔 +1
            elif bill == 10:  # 顧客手拿10元鈔
                if d5==0:  # 若沒辦法找零，糟
                    return False
                d10 += 1  # 拿到1張10元
                d5 -= 1  # 用掉1張5元
            elif bill == 20:  # 顧客手拿20元鈔
                if d5>0 and d10>0:  # 可找零
                    d20, d10, d5 = d20+1, d10-1, d5-1
                elif d5>=3:  # 找3張5元鈔
                    d20, d5 = d20+1, d5-3
                else:  # 不夠零錢找，糟
                    return False
        return True  # 順利結束，開心
