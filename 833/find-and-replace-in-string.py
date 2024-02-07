# 有 k 組 indices, source, target
# 要在 s 裡做 k 組 replace，能做就做，不能就跳掉
# 保證不會有重疊的狀況
# 可依照 indices 排序，再照 source 的長度，將 s 裁成多段
# 最後再把對應項取代
class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        k = len(indices)
        op = [[indices[i],sources[i],targets[i]] for i in range(k)]
        op.sort() # 照著 indices 排序
        # print(op)
        prev = 0 # 前一項的結尾位置
        s2 = [] # 將 s 裁成 2*k 段
        for i in range(k):
            lenNow = len(op[i][1])
            if s[op[i][0]:op[i][0]+lenNow]==op[i][1]: # 有比對到，才能斷字
                s2.append(s[prev:op[i][0]]) # 中間不動
                s2.append(op[i][2]) # 比對到，就取代
                prev = op[i][0]+lenNow # 更新裁完的位置
        s2.append(s[prev:]) # 最後剩下的那段
        # print(s2)
        return ''.join(s2)
# case 5/57: [3,5,1]
# ["kg","ggq","mo"]
# ["s","so","bfr"] 小心排序後，要改用排序後的字串
# case 52/57: [2,2] 什麼！竟然重疊！
# ["cdef","bc"]
# ["f","fe"]
# 題目是說「有取代的話，保證沒有overlapping」所以「要取代」才斷字
