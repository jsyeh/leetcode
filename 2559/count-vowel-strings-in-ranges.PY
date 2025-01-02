# LeetCode 2559. Count Vowel Strings in Ranges
# words[i] 裡由母音（a e i o u）開頭、結尾的字，有幾個？
# queries[i] 裡 [left, right] 對應 words[left]...words[right] 範圍內「合格」的字
class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowel = set(['a','e','i','o','u'])  # 快速找出「母音」
        # 先針對「母音開頭、結尾」建立 prefix sum 統計有幾個
        preSum = [0]  # 利用 prefix sum 累積「有幾個合格的字」
        for word in words:
            if word[0] in vowel and word[-1] in vowel:
                preSum.append(preSum[-1]+1)  # 合格的字 +1
            else:  # 不合格的字
                preSum.append(preSum[-1])  # 照舊
        ans = []
        for left, right in queries:  # 針對每一次 query 詢問
            ans.append( preSum[right+1] - preSum[left] )
            # 利用減法，快速知道「範圍內」有幾個合格的字
        Treturn ans
