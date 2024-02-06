# same shift 的意思，是只要「每個字母一起shift」會重覆
# 其實就變成整數後，減掉第1個數字，便是對應的值
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        def shiftBack(s): # 負責把字串s 變成 0..25 的一堆數字「串起來」
            ans = [str((ord(s[i])-ord(s[0])+26)%26) for i in range(len(s))]
            return ' '.join(ans) # 對應 s[i]-s[0] 再換到 0..25 的數字 串起來

        shiftStrings = [(shiftBack(s),s) for s in strings]
        shiftStrings.sort() # 根據 shiftBack()退回到 0 開頭的數字字串，去排序
        # print(shiftStrings) 

        ans = [[shiftStrings[0][1]]]
        for i in range(1,len(shiftStrings)): # 排序後，相同的字會放在一起
            if shiftStrings[i][0]==shiftStrings[i-1][0]:
                ans[-1].append(shiftStrings[i][1]) # 與前字相同，就同一國
            else: # 與前字不同
                ans.append([shiftStrings[i][1]]) # 就創新的國
        return ans
