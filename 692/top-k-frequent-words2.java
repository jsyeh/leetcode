class Solution {
    public List<String> topKFrequent(String[] words, int k) {
        HashMap<String,Integer> map = new HashMap<String,Integer>();
        for(int i=0; i<words.length; i++) {
            if(map.containsKey(words[i])) {
                map.put(words[i], map.get(words[i])+1);
            } else map.put(words[i], 1);
        }

        PriorityQueue<String> heap = new PriorityQueue<String>(words.length, (a,b) -> (map.get(a)==map.get(b))? a.compareTo(b) : map.get(b)-map.get(a));
        for(String word : map.keySet()) {
            heap.add(word);
        }


        List<String> ans = new ArrayList<String>();
        for(int i=0; i<k; i++) {
            ans.add(heap.poll());
        }

        return ans;
    }
    /*
    public List<String> topKFrequent(String[] words, int k) {
        Map<String,Integer> map = new HashMap<String,Integer>();
        PriorityQueue<String> heap = new PriorityQueue<String>(words.length, new Compare(map));
        for(int i=0; i<words.length; i++){
            if(map.containsKey(words[i])){
                map.put(words[i], map.get(words[i])+1);
            }else{
                map.put(words[i], 1);
            }
            System.out.println(words[i] + " " + map.get(words[i]));
        }
        //then find top k integers
        List<String> ans = new ArrayList<String>();
        for( Map.Entry<String,Integer> one : map.entrySet()){
            heap.add(one.getKey());
        }
        for(int i=0; i<k; i++){
            ans.add(heap.poll());
        }
        return ans;
    }
}
class Compare implements Comparator<String> {
    Map<String,Integer> map;
    Compare(Map<String,Integer> _map){
        map = _map;
    }
    public int compare(String a, String b){
        int i1 = map.get(a), i2 = map.get(b);
        if(i1==i2) return  a.compareTo(b);
        return - (map.get(a) - map.get(b));
    }*/
}
