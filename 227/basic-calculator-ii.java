class Solution {
    public int calculate(String s) {
        Stack<Integer> stack = new Stack();
        int k = 0; //k代表數字
        char prev = '+'; //這個技巧，可讓程式變簡單，等於每個數字前面都有個運算符號
        for(int i=0; i<s.length(); i++){
            //還沒想好怎麼寫，尤其是把字串變成 stack 的部分
            if(s.charAt(i)==' ' && i!=s.length()-1) continue;
            boolean isDigit = s.charAt(i)>='0' && s.charAt(i)<='9';
            if(isDigit) {
                k = k * 10 + (s.charAt(i)-'0');
            }
            
            if((!isDigit) || i==s.length()-1 ){ //遇到結束時，也要清算
System.out.println(prev);
                if(prev=='+'){
                    stack.push(k);
                }else if(prev=='-'){
                    stack.push(-k);
                }else if(prev=='*'){
                    stack.push(stack.pop()*k);
                }else if(prev=='/'){
                    stack.push(stack.pop()/k);
                }
                prev = s.charAt(i); //準備好下一個數字前面的運算符號
                k = 0;
            }
        }
        int ans = 0;
        while(stack.size()>0) {
System.out.println("ans:"+ans);
            ans += stack.pop();
        }
        return ans;
    }
}
