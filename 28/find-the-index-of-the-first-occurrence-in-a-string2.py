# week01-2.py LeetCode 學習計畫 Python 版本1 for迴圈
# LeetCode 28. Find the Index of the First Occurrence in a String
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        H = len(haystack)  # 字串長度
        N = len(needle)    # 字串長度
        # sadbutsad
        # sad i:0
        #  sad i:1
        # ....
        #       sad i:6
        for i in range(H-N+1):  # 長度9 找 長度3 有 0...6 共7格
            if haystack[i:i+N] == needle:  # 若兩個相同
            # 把字串,從i開始,取到 i+N 結束 共 N 個字
                return i  # 成功找到位置
        return -1  # 沒有成功
