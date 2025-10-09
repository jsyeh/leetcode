# LeetCode 3494. Find the Minimum Amount of Time to Brew Potions
# 一堆巫師「合作接力」製作藥水，像工廠流水線一樣的運作，順序不能有錯。
# 其中巫師i製作藥水j的花費時間, 是技能 skill[i] * 藥水j的法力 mana[j]
# 可調整「開始製作藥水j的時間」讓巫師間沒有間隔, 想最快完成全部藥水的製作
class Solution:
    def minTime(self, skill: List[int], mana: List[int]) -> int:
        W, P = len(skill), len(mana)  # 巫師數量W、藥水數量P
        freeTime = [0] * W  # 每位巫師有空的時間點
        for j in range(P):  # 依序製作藥水
            T = 0  # 模擬看看吧！針對藥水j 從頭到尾走一次
            freeTime2 = [0] * W  # 記錄製作藥水j 過程的「詳細時間」
            delay = 0  # 記錄時間差，將對應「什麼時候開始」能讓「巫師間沒有間隔」完成藥水j
            for i in range(W):  # 更新每位巫帥「有空的時間點」
                T = T + skill[i] * mana[j]  # 模擬「巫師i」製作「藥水j」的結束時間
                freeTime2[i] = T  # 記錄「每一站」的模擬時間，下面則是「現實」的delay時間差
                delay = max(delay, (freeTime[i] + skill[i] * mana[j]) - freeTime2[i])
            for i in range(W):  # 把delay時間差，逐個加入，得到準確的「完成時間」
                freeTime[i] = freeTime2[i] + delay
        return freeTime[W-1]  # 最後一位巫師「完成」藥水的時間
