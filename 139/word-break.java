class Solution {
    HashSet<String> dict = new HashSet<String>();
    public boolean wordBreak(String s, List<String> wordDict) {
        for(String word : wordDict) {
            dict.add(word);
        }
        table = new int[s.length()+1];
        return wordBreak(s, 0);
    }
    int [] table; //0: none, 1: true, 2: false
    boolean wordBreak(String s, int start) {
        if(start>=s.length()) return true;
        if(table[start]==1) return true;//0: none, 1: true, 2: false
        if(table[start]==2) return false;
        boolean ans=false;
        //for(int i=start; i<s.length(); i++) {
        int i = start;
            for(int k=i+1; k<i+20 && k<s.length()+1; k++) {
                String word = s.substring(i,k); //右不包含
                if(dict.contains(word)) {
                    //if(k==s.length()) return true;
                    boolean temp = wordBreak(s, k);
                    if(temp) ans = true;
                }
            }
        //}
        if(ans==true) table[start] = 1;
        else table[start] = 2;
        return ans;
    }
}
