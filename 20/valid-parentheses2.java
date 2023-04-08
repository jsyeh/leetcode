class Solution {
    public boolean isValid(String s) {
        ArrayList<Character> stack = new ArrayList<Character>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='(' || c=='{' || c=='[') stack.add(c);
            else if(c==')' && pop(stack)!='(') return false;
            else if(c=='}' && pop(stack)!='{') return false;
            else if(c==']' && pop(stack)!='[') return false;
        }
        if(stack.size()==0) return true;
        return false;
    }
    char pop(ArrayList<Character>stack){
        if(stack.size()<=0) return ' ';//bad
        char last = stack.get(stack.size()-1);
        stack.remove(stack.size()-1);
        return last;
    }
}//Case 4: "["
//Case 5: "]"
//Case 6: "([}}])"
