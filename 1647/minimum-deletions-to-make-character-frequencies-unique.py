# good：每種字母出現的頻率都不同
class Solution:
    def minDeletions(self, s: str) -> int:
        # 先統計（原本）字母出現的頻率
        freq = {}
        for c in s:
            if c in freq:
                freq[c] += 1
            else:
                freq[c] = 1
        
        # 接下來排序，再從大到小，看要如何delete
        arr = []
        for c in freq:
            arr.append(freq[c])
        arr.sort()
        print(arr)
        # 從大到小巡，如果沒照順序，就更新ans 並將arr[i-1]更正
        ans = 0
        for i in range(len(arr)-1, 0, -1):
            if arr[i-1]>=arr[i]:
                if arr[i]==0:
                    ans += arr[i-1]
                    arr[i-1] = 0
                else:
                    ans += arr[i-1]-arr[i] + 1
                    arr[i-1] = arr[i] - 1
        return ans
# case 65/103: "bbcebab" 遇到只有1個的字母，刪掉就好，不用管太多
# case 79/103: "beaddedbacdcd" 遇到 arr[i] ==0 的話，只要 += arr[i-1] 即可
