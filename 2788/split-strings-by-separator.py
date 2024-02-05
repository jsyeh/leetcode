class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        now = separator.join(words).split(separator)
        ans = []
        for w in now:
            if w!='': ans.append(w)
        return ans 
