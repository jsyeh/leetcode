# 摩斯電碼 Morse Code 可能翻譯出「相同」的碼，測有多少「不同」的碼
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morse = {'a':".-",'b':"-...",'c':"-.-.",'d':"-..",'e':".",'f':"..-.",'g':"--.",'h':"....",'i':"..",'j':".---",'k':"-.-",'l':".-..",'m':"--",'n':"-.",'o':"---",'p':".--.",'q':"--.-",'r':".-.",'s':"...",'t':"-",'u':"..-",'v':"...-",'w':".--",'x':"-..-",'y':"-.--",'z':"--.."}
        output = set()
        for word in words: # 每個字，都組合看看
            line = ''
            for c in word: # 逐個字母組合
                line += morse[c]
            output.add(line) # 組出1行電碼，放入 output 集合
        return len(output) # 看有多少不同的碼
