# 數字出現的「次數」不會重覆
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        occur = defaultdict(int)
        for num in arr: # 先針對每個數字，統計出現次數
            occur[num] += 1 # num 這個數字「出現次數」+1

        happened = set() # 出現「次數」 有重覆出現過嗎 
        for num in occur: # 再針對每個數字，看「出現次數」有沒有重覆
            if occur[num] in happened: # 竟然出現過了，那就不對了
                return False
            else: # 沒出現過的話，很好
                happened.add(occur[num]) # 把這個「次數」記錄下來
        return True # 一切都沒問題的話，就是成功
