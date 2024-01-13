# 兩字串間，要交換幾次，可讓兩字串完全一樣？
# 字串長度相同，長度<=1000，字母只會出現 x 和 y
# 可用些greedy的想法來做
# (1)每個字母統計次數，出現次數必須偶數
# (2)規則：type1「有幾個x變y」、type2「有幾個y變x」
# (3) type1//2 可交換一半解決
#     type2//2 可交換一半解決
# 但落單的如 example 2 ，就要 換換2次才能解
class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        counterAll = Counter(s1) + Counter(s2)
        #print(counterAll)
        for v in counterAll.values():
            if v%2!=0: return -1 # 偶數才能平均分配

        type1, type2 = 0, 0
        for i in range(len(s1)):
            if s1[i]=='x' and s2[i]=='y':
                type1 += 1
            if s1[i]=='y' and s2[i]=='x':
                type2 += 1
        #print(type1, type2)
        if type1%2==1: 
            return type1//2+type2//2+2
        return type1//2+type2//2
# case 36/70: 
# "xxyyxyxyxx"
# "xyyxyxxxyx"
