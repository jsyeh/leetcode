# 要把 current 的時間, 調成 correct 的時間 (保證 current<=correct)
# 能做的操作有 +60 +15 +5 +1 這幾種, 所以就很像「找零錢」的題目
class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def timeToMinute(s:str)->int: # 可把時間格式 轉換成 第幾分鐘
            hh, mm = s.split(':')
            return int(hh)*60 + int(mm)

        diff = timeToMinute(correct) - timeToMinute(current)
        return diff//60 + (diff%60)//15 + (diff%15)//5 + (diff%5)
