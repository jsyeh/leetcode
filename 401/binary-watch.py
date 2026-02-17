# LeetCode 401. Binary Watch
# 用4個LED(8,4,2,1)表示0-11小時、用6個LED(32,16,8,4,2,1)表示0-56分鐘
# 二進位算時間：turnedOn 有幾個LED亮，列出全部可能的時間。用「排列組合」即可
class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        ans = []  # 用字串形式，將全部可能的時間，放入「答案陣列」
        for hourLED in range(min(turnedOn+1, 4+1)):  # hour的LED數
            minuteLED = turnedOn - hourLED  # 換算出 minute的LED數
            # 接下來利用 combinations() 依 LED 數，算出「排列組合」的結果
            for h in combinations([8,4,2,1], hourLED):  # 排列組合
                hh = sum(h)  # 依「亮的LED」算出總和 hh 值
                if hh > 11: continue  # 0-11 才正確，超過就換下一組
                for m in combinations([32,16,8,4,2,1], minuteLED):
                    mm = sum(m)  # 依「亮的LED」算出總和 mm 值
                    if mm > 59: continue  # 0-56 才正確，超過就換下一組
                    ans.append(str(hh) + ':' + str(mm).zfill(2))
                    # 題目要求 hh 前面不能有0，但mm要用0補齊2位
        return ans
