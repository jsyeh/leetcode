# LeetCode 1488. Avoid Flood in The City
# rains[i] 0 代表沒下雨、1 開始的值代表「雨將下在某個湖」
# 湖是空的 -> 下雨會積水 -> 再次下雨將有「大災難」。要在「再次下雨」前，處理積水
# 可記錄「晴天」。若事先知道「某個湖」將有「大災難」，在「積水後的晴天」先清理它
class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        N = len(rains)  # 總共有 N 天
        ans = [-1] * N  # 所有的「下雨天」一開始「都不去處理積水」
        sunny = []  # 有哪些天是「sunny晴天」可處理積水。「沒效率」改用 SortedList()更好
        lakeFull = {}  # 某個湖，是在哪一天積水
        for i, lake in enumerate(rains):  # 第i天，下雨下在哪一個湖
            if lake==0:  # 晴天「一定要挑1個湖來清」
                sunny.append(i)  # 記錄「sunny晴天」，以後可以用
                ans[i] = 1  # 目前還無法預知「誰將有大災難」先隨便挑個湖來清
            elif lake not in lakeFull:  # 「這個湖lake」還沒積水，安全
                lakeFull[lake] = i  # 標註「這個湖lake」在第 i 天「下雨積水」
            else:  # 糟！「這個湖lake」積水已滿，需要「事先」找時間處理「越早越好」
                ii = bisect_left(sunny, lakeFull[lake])  # 滿水後，第一個「sunny晴天」
                if ii >= len(sunny):  # 啊！在 sunny days 裡，找不到「能施工」的晴天
                    return []  # 沒辦法完成任務、失敗
                day = sunny[ii]  # 有找到的話，是「哪一個sunny晴天」要處理啊！
                ans[day] = lake  # 這天就保留給「這個湖lake」吧！
                sunny.remove(day)  # 用掉這個「sunny晴天」。「沒效率」改用 SortedList()更好
                lakeFull[lake] = i  # 事先清好後，第i天下雨，換第i天積水
        return ans
