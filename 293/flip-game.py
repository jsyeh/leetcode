# 請在 currentState 裡，挑任意2個相連的++ 變 --
# 把全部的可能，都放入 ans 裡
class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:
        ans = []
        for i in range(len(currentState)-1): # 因i,i+1 都變+,所以 -1
            # 要檢查，有'++'才能變成'--
            if currentState[i:i+2]=='++':
                ans.append(currentState[0:i]+'--'+currentState[i+2:])
        return ans
# case 4/24: "--"
