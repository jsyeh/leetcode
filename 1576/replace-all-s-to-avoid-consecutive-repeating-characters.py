# 這題有超多種可能的答案的，任一種都行
# 把 '?' 換任何字母，只要「相鄰字母不連續」就可以了
class Solution:
    def modifyString(self, s: str) -> str:
        s = list(s) # 先轉成 list 以便修改
        N = len(s)
        for i in range(N):
            if s[i]=='?':
                # 遇到 '?' 要三思而後行，左右比較一下避開即可
                if s[i-1]!='a' and s[(i+1)%N]!='a':
                    s[i] = 'a' # 可能放 'a'
                elif s[i-1]!='b' and s[(i+1)%N]!='b':
                    s[i] = 'b' # 可能放 'b'
                elif s[i-1]!='c' and s[(i+1)%N]!='c':
                    s[i] = 'c' # 可能放 'c' # 三種就夠用了
            # 其他正常字母，直接用，不用改
        return ''.join(s)
# case 696/776: "j?qg??b" 連續兩個? 容易錯誤
# case 770/776: "a?c" 我竟然也錯，我太爛了
