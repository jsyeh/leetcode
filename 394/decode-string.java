class Solution {
    public String decodeString(String s) {
        String now = "";
        int k=0;
        LinkedList<Integer> stack_k = new LinkedList<Integer>();
        LinkedList<String> stack_now = new LinkedList<String>();
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c>='0' && c<='9') {
                k = k*10 + c-'0';
            } else if(c=='[') {
                stack_k.push(k);
                stack_now.push(now);
                k=0;
                now="";
            } else if(c==']') {
                k = stack_k.pop();
                String temp="";
                for(int j=0; j<k; j++){
                    temp += now;
                }
                now = stack_now.pop() + temp;
                k = 0;
            } else {
                now += c;
            }
        }
        return now;

        /*
        String ans = "", now = "";
        LinkedList<Integer> stack_from = new LinkedList<Integer>();
        LinkedList<String> stack_string = new LinkedList<String>();
        LinkedList<Integer> stack_k = new LinkedList<Integer>();
        LinkedList<Integer> stack_state = new LinkedList<Integer>();
        //每次遇到 '[' 就將 k, from, string(備份前一層的字串) 都加入 stack。 string會慢慢長大。
        int k=0;
        int state = 0; //0: calc k, 1:inside string []
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c>='0' && c<='9'){
                k = k*10 + c-'0';
            }else if(c=='['){
                stack_from.push(i+1);
                stack_string.push(now);
                stack_state.push(state);
                stack_k.push(k);
                state = 1;
                now = "";
                k=0;
            }else if(c==']'){
                int start = stack_from.pop();
                k = stack_k.pop();
                for(int j=0; j<k; j++){
                    //ans += s.substring(start, i);
                    ans += now;
                }
                state = 0;
                k = 0;
                now = stack_string.pop();
                state = stack_state.pop();
            }else {
                now += c;
            }
        }
        ans += now;
        return ans;*/
    }
}
