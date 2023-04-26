class Solution {
    public List<List<Integer>> combinationSum2(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        combinate(candidates, target, 0, ans, list);
        return ans;
    }

    void combinate(int[] candidates, int target, int start, List<List<Integer>> ans, List<Integer> list) {
        if(target<0) return;
        if(target==0) {
            List<Integer> temp = new ArrayList<Integer>(list);
            ans.add(temp);
            return;
        }
        int prev = Integer.MIN_VALUE;
        for(int i=start; i<candidates.length; i++) {
            if(prev==candidates[i]) continue;
            prev = candidates[i];

            if(target-candidates[i]<0) return; //加起來越過，不要用，後面也不用了
            list.add(candidates[i]);
            combinate(candidates, target-candidates[i], i+1, ans, list);
            list.remove(list.size()-1);
        }
    }
}
