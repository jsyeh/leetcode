//因為去年寫的 Java 程式使用字串的 + 很沒有效率，所以我重寫
//改用 char [] s2 = s.toCharArray() 及 String(s2).replace("-", ""); 想加速
//好像 StringBuilder ans = new StringBuilder(); 配合 ans.append(c) 再 ans.toString() 也可以
class Solution {
    public String minRemoveToMakeValid(String s) {
        char [] s2 = s.toCharArray();
        Stack<Integer> stack = new Stack<Integer>(); //存括號的index
        for(int i=0; i<s2.length; i++){
            if(s2[i]=='(')  stack.push(i); // 上括號
            else if(s2[i]==')'){ // 下括號
                if(stack.size()>0){
                    stack.pop(); // 可以順利配對掉，不用處理
                }else{
                    s2[i] = '-'; // 無法配對，將需要刪除這個下括號

                }
            }
        }
        //處理完後，將 stack 裡的上括號清掉
        for(Integer i : stack){
            s2[i] = '-'; //無法配對的上括號，將要清掉
        }
        return new String(s2).replace("-", "");
    }
}//case 13/62: "())()((("
