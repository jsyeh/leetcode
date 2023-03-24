class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        List<List<String>> groups = new ArrayList<List<String>>();
        Map<String, Integer> map = new HashMap<String, Integer>();
        for(int i=0; i<strs.length; i++){
            String key = sortString(strs[i]);
            if(map.containsKey(key)) {
                int groupI = map.get(key);
                groups.get(groupI).add(strs[i]);
            } else {
                ArrayList<String>  oneGroup = new ArrayList<String>();
                oneGroup.add(strs[i]);
                int groupI = groups.size();
                groups.add(oneGroup);
                map.put(key, groupI);
            }
        }
        return groups;
    }
    String sortString(String line) {
        char [] str = line.toCharArray();
        Arrays.sort(str);
        return new String(str);
    }
}
