class Solution {
    public boolean isValid(String s) {
        int N = s.length();
        char [] stack = new char[N];
        int top=0;
        for(int i=0; i<N; i++){
            char c = s.charAt(i);
            if(c=='(') stack[top++]='(';
            else if(c=='[') stack[top++]='[';
            else if(c=='{') stack[top++]='{';
            else if(c==')') {
                if(top>0 && stack[top-1]=='(') top--;
                else return false;
            }else if(c==']') {
                if(top>0 && stack[top-1]=='[') top--;
                else return false;
            }else if(c=='}') {
                if(top>0 && stack[top-1]=='{') top--;
                else return false;
            }
        }
        if(top==0) return true;
        else return false;
    }
}
//Case 4: "["
//Case 5: "]"
//Case 6: "([}}])"
