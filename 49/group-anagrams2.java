class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> ans = new ArrayList<List<String>>();
        HashMap<String,ArrayList<String>> map = new HashMap<String,ArrayList<String>>();
        for(String word : strs){
            String key = sortString(word);
            if(map.containsKey(key)){
                ArrayList<String> list = map.get(key);
                list.add(word);
                map.put(key, list);
            }else{
                ArrayList<String> list = new ArrayList<String>();
                list.add(word);
                map.put(key, list);
            }
        }
        for(String key : map.keySet()){
            ArrayList<String> list = map.get(key);
            ans.add(list);
        }
        return ans;
    }
    String sortString(String input) {
        char [] line = input.toCharArray();
        Arrays.sort(line);
        return new String(line);
    }
}
