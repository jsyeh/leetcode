# LeetCode 3043. Find the Length of the Longest Common Prefix
# arr1 arr2 挑「兩兩一組」找「最長的prefix」。不能用暴力法兩層for迴圈，因 5*10^4 數字太多
# 可幫 arr1 建立 prefixSet 有全部 prefix，再用 arr2 測「最長」的重覆prefix答案
class Solution:
    def longestCommonPrefix(self, arr1: List[int], arr2: List[int]) -> int:
        prefixSet = set()  # 放 arr1 「每個數」的全部 prefix
        for num in arr1:  # 把 arr1 每個數，都建立 prefix1 set
            s = str(num)  # 轉成字串，以便「高到低」位數「逐一找出prefix」
            prefix = ''
            for c in s:
                prefix += c  # 逐一增長 prefix
                prefixSet.add(prefix)
        # 再將 arr2 逐一比對，看「是否prefix 有在 prefix1裡」
        ans = 0
        for num in arr2:  # 程式很相似
            s = str(num)  # 程式很相似
            prefix = ''  # 程式很相似
            for c in s:  # 程式很相似
                prefix += c  # 程式很相似
                if prefix not in prefixSet:
                    break  # prefixSet 裡沒有，就不用再做了
                ans = max(ans, len(prefix))
        return ans
