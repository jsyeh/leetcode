class Solution {
    public int minTransfers(int[][] transactions) {
        Map<Integer,Integer> map = new HashMap<>();
        for(int[] t : transactions) {
            if(map.containsKey(t[0])){
                map.put(t[0], map.get(t[0]) - t[2]);
            }else map.put(t[0], -t[2]);
            if(map.containsKey(t[1])){
                map.put(t[1], map.get(t[1]) + t[2]);
            }else map.put(t[1], t[2]);
        }

        return findAns(0, new ArrayList<>(map.values()) );
    }

    int findAns(int start, List<Integer> b) {
        while( start < b.size() && b.get(start) == 0) start ++;

        if(start == b.size()) return 0;

        int ans = Integer.MAX_VALUE;
        for(int i=start+1; i<b.size(); i++){
            if(b.get(start) * b.get(i)<0) {
                b.set(i, b.get(i)+b.get(start));
                int temp = 1 + findAns(start+1, b);
                if(temp<ans) ans = temp;
                b.set(i, b.get(i)-b.get(start));
            }
        }
        return ans;
    }
}
