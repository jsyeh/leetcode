# words 裡有 "prev" 或數字對應的字串
# prev 時，要把「最後的整數」加到ans裡
# 因數字不多，暴力法可行
# 遇到 prev 時，持續記錄，可用 -1 -2 之類來取整數
class Solution:
    def lastVisitedIntegers(self, words: List[str]) -> List[int]:
        ans = [] # 用來放「呼叫prev」時得到的整數
        allInt = [] # 用來放目前輸入的整數
        allIntIndex = 0 # 用來決定 prev 時，對應 allInt 的位置，會用「負數」來倒數
        for word in words:
            if word == 'prev': # 要往前
                allIntIndex += 1
                if allIntIndex > len(allInt): # 如果數字倒退太多
                    ans.append(-1) # 就塞入 -1
                else: # 正常範圍內的話
                    ans.append(allInt[-allIntIndex]) # 把倒數的數字加入
            else: # 是整數
                allIntIndex = 0
                allInt.append(int(word))
        return ans
