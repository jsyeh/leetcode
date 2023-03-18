class Solution {
    List<String> ans;
    public List<String> generateParenthesis(int n) {
        ans = new ArrayList<String>();
        func(ans, n, 0, 0, "");
        return ans;
    }
    void func(List<String> ans, int n, int left, int right, String line) {
        if(right==left && left==n){
            ans.add(line);
            return;
        }
        if(left<n){
            func(ans, n, left+1, right, line+"(");
        }
        if(right<left){
            func(ans, n, left, right+1, line+")");
        }
    }
}
