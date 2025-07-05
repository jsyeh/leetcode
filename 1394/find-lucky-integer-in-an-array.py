# LeetCode 1394. Find Lucky Integer in an Array
# lucky 整數：「數值」剛好與「出現次數」相同，找最大的lucky 整數
class Solution:
    def findLucky(self, arr: List[int]) -> int:
        counter = Counter(arr)  # 利用 Counter()來統計「出現次數」
        ans = -1  # 預設的答案
        for n in counter:  # 依照統計結果，逐一比較
            if n==counter[n]:  # lucky! 「數值」剛好與「出現次數」相同
                ans = max(ans, n)  # 找最大值
        return ans
