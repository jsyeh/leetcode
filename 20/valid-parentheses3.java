class Solution {
    Stack<Character> stack = new Stack<Character>();
    public boolean isValid(String s) {
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='{' || c=='(' || c=='[') stack.push(c);
            else if(c=='}'){
                if(stack.size()<=0) return false;
                if(stack.pop()!='{') return false;
            }else if(c==']'){
                if(stack.size()<=0) return false;
                if(stack.pop()!='[') return false;
            }else if(c==')'){
                if(stack.size()<=0) return false;
                if(stack.pop()!='(') return false;
            }
        }
        if(stack.size()==0) return true;
        else return false;
    }
}
