class Solution {
    ArrayList<Character> array = new ArrayList<Character>();
    public String removeStars(String s) {
        for(int i=0; i<s.length(); i++){
            char c = s.charAt(i);
            if(c=='*') array.remove(array.size()-1);
            else array.add(c);
        }
        String ans = "";
        for(int i=0; i<array.size(); i++){
            ans += array.get(i);
        }
        return ans;
    }
}
