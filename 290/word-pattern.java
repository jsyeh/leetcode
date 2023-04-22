class Solution {
    public boolean wordPattern(String pattern, String s) {
        String [] words = s.split(" ");
        if(pattern.length()!=words.length) return false;

        HashMap<String,Character> map = new HashMap<String,Character>();
        HashMap<Character,String> map2 = new HashMap<Character,String>();

        for(int i=0; i<words.length; i++) {
            char c = pattern.charAt(i);
            String word = words[i];
            if(map.containsKey(word)){
                if(map.get(word)==c && map2.containsKey(c) && map2.get(c).equals(word)){ }//很好,整套都正確
                else return false;
            }else{
                if(map2.containsKey(c)) return false;
                map.put(word,c);
                map2.put(c,word);
            }
        }
        return true;
    }
}
