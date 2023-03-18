class Solution {
    char[][]table={
        {},
        {},
        {'a','b','c'},
        {'d','e','f'},
        {'g','h','i'},
        {'j','k','l'},
        {'m','n','o'},
        {'p','q','r','s'},
        {'t','u','v'},
        {'w','x','y','z'}
    };
    List<String> ans;
    public List<String> letterCombinations(String digits) {
        ans = new ArrayList<String>();
        int N = digits.length();
        if(N==0) return ans;
        
        func(0, N, "", digits);
        return ans;
    }
    void func(int now, int N, String nowAns, String digits){
        int d = digits.charAt(now)-'0';
        for(int k=0; k<table[d].length; k++){
            if(N-now==1){
                ans.add(nowAns+table[d][k]);
            }else{
                func(now+1, N, nowAns+table[d][k], digits);
            }   
        }
    }

}
