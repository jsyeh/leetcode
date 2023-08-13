# 可模仿 C字串的 \n \\ 之類的技巧，利用 || |n 來當特殊字元
class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        ans = "" # 慢慢累積答案
        for line in strs:
            temp = "" # 每一行字，慢慢累積進來
            for c in line:
                if c=="|": c = "||" # 累積跳脫字元
                temp += c
            ans += temp + "|n" # 每個字串結尾，加上 "|n"
        return ans
        

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        # print(s)
        ans = [] # 用來收很多字串，ans.append(line)
        N = len(s)
        line = ""
        escape = False
        for i in range(N):
            if escape: # 不像C的for迴圈可用 i++ 多跳1字
                escape = False # 所以加個 escape變數
                continue # 跳掉避開特殊字的第2個字母
            if s[i]=="|": # 特殊字，有兩個狀況
                if s[i+1]=="n": # (1) 字串結尾
                    ans.append(line)
                    line = "" # 字串結尾
                    escape = True # 迴圈跳掉避開下個字母
                else: # ||有跳脫字元，先加|，下次跳掉避開
                    line += s[i]
                    escape = True # 迴圈跳掉避開下個字母
            else: line += s[i]
        
        return ans

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
