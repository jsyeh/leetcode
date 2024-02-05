# 有些位數'?'隱藏，問「最大的數」有多大
class Solution:
    def maximumTime(self, time: str) -> str:
        time = list(time)
        hh, mm = time[:2], time[3:]
        if mm[1]=='?': mm[1] = '9'
        if mm[0]=='?': mm[0] = '5'

        if hh[0]=='0' and hh[1]=='?': hh[1] = '9'
        elif hh[0]=='1' and hh[1]=='?': hh[1] = '9'
        elif hh[0]=='2' and hh[1]=='?': hh[1] = '3'
        elif hh[0]=='?' and hh[1]=='?': hh = ['2','3']
        elif hh[0]=='?' and '0'<=hh[1]<='3': hh[0] = '2'
        elif hh[0]=='?' and '4'<=hh[1]<='9': hh[0] = '1'
        return ''.join(hh)+':'+''.join(mm)
