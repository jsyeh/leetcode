# LeetCode 2273. Find Resultant Array After Removing Anagrams
# 將 words「相鄰的 anagrams（用相同字母）」移掉後面那個，直到「找不到相鄰 anagrams 為止」
class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        ans = []  # 因為剛剛速度太慢，決定再寫一個版本試試
        for word in words:  # 逐一取出，看是否要「放入 ans 裡」
            if len(ans)==0 or Counter(ans[-1])!=Counter(word):
                ans.append(word)  # 沒辦法「對消」就放入 ans 裡
        return ans
