class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        N = len(strs) # 有幾個字串
        sortedStr = [(sorted(s),s) for s in strs] # 左排序、右原字串
        # sortedStr[i][0] 字母排序後的字串 sortedStr[i][1] 原字串
        sortedStr.sort() # 再依「字母排序後的字串」來排序「全部」字串

        ans = []
        ans.append([sortedStr[0][1]]) # 把最小字串放最前面的list
        for i in range(1,N):
            if sortedStr[i][0]==sortedStr[i-1][0]: # 同一國的話
                ans[-1].append(sortedStr[i][1]) # 就放在一起
            else: # 不同國的話
                ans.append([sortedStr[i][1]]) # 就開新的list
        return ans
