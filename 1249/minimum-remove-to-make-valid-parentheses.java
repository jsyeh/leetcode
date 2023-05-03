class Solution {
    public String minRemoveToMakeValid(String s) {
        Stack<Character> stackChar = new Stack<Character>();
        Stack<String> stackString = new Stack<String>();

        String word = "";
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='(') {
                stackChar.push(c);
                stackString.push(word);
                word = "";
            } else if(c==')') {
                if(stackChar.size()>0) { //合理的括號
                    word = stackString.pop() + '(' + word + ')';
                    stackChar.pop();
                    //word = "";
                } else { //不合理的括號，就當作沒看到

                }
            } else {
                word += c;
            }
        }
        //字串結束時，省略全部的上括號'('
        while(stackString.size()>0) {
            word = stackString.pop() + word;
        }
        return word;
    }
}//case 13/62: "())()((("
