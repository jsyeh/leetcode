# 有一堆水龍頭（澆水範圍不同），需要幾個水龍頭，才能把 0...n 都澆到水
# 如果沒全部照顧到 就要 return -1
class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        table = [inf]*(n+1) 
        # table[i] 到0...i範圍全部照顧到，「共需幾個水龍頭」
        table[0] = 0 # 0...0 長度為0的區域，需要0個tap
        for i in range(n+1): # 因題目的 len(ranges) 是 n+1
            r = ranges[i] # 這次 tap i 可照顧到的距離，照顧 i-r..i+r
            left, right = max(0, i-r), min(n, i+r)
            print(i, left, right)
            for k in range(left, right+1): # 逐一巡tap i 可澆的範圍
            # 想法：0...k只要開table[k]個tap, 再配上 tap i 便能照顧到最right
                if table[k]+1 < table[right]:
                    table[right] = table[k] + 1 # 所以 table[k] + 1
            # print(table)
        if table[n] == inf: # 若 0...n 全部照顧到，竟然需要 inf個，那沒救
            return -1
        return table[n] # 這個，能照顧到 0...n
