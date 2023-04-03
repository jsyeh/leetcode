class Solution {
    public List<List<Integer>> generate(int numRows) {
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        ArrayList<Integer> one = new ArrayList<Integer>();
        one.add(1);
        ans.add(one);
        for(int level = 1; level<numRows; level++) {
            ArrayList<Integer> next = new ArrayList<Integer>();
            List<Integer> prev = ans.get(level-1);
            next.add(1);
            for(int i=1; i<level; i++){
                next.add(prev.get(i-1) + prev.get(i));
            }
            next.add(1);
            ans.add(next);
        }
        return ans;
    }
}
