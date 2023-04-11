class Solution {
    public List<String> letterCasePermutation(String s) {
        String s2 = "";
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c>='A' && c<='Z') s2 += (char)(c-'A'+'a');
            else s2 += c;
        }
        return perm(s2);
    }
    List<String> perm(String s) {
        List<String> ans = new ArrayList<String>();
        if(s.length()==0){
            ans.add("");
            return ans;
        }
        char c = s.charAt(0);
        List<String> subAns = perm(s.substring(1));
        for(String s2 : subAns){
            ans.add("" + c + s2);
            if(c>='a' && c<='z') {
                char c2 = (char) (c - 'a' + 'A');
                ans.add("" + c2 + s2);
            }
        }
        return ans;
    }
}
