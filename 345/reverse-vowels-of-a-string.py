class Solution:
    def reverseVowels(self, s: str) -> str:
        N = len(s)
        vowel = []
        for i in range(N):
            c = s[i]
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                vowel.append(c) # 將母音都收集好
            elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                vowel.append(c) # 將大寫母音都收集好
        
        # 下面再巡一次，子音（照塞）、母音（倒著pop()來塞）
        ans = [0]*N
        for i in range(N):
            c = s[i]
            if c=='a' or c=='e' or c=='i' or c=='o' or c=='u':
                ans[i] = vowel.pop()
            elif c=='A' or c=='E' or c=='I' or c=='O' or c=='U':
                ans[i] = vowel.pop()
            else:
                ans[i] = c
        return "".join(ans)
# case 290/480: "aA" 有大寫、小寫
