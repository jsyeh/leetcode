class Solution {
    public List<List<Integer>> combinationSum(int[] candidates, int target) {
        Arrays.sort(candidates);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        List<Integer> list = new ArrayList<Integer>();
        combinate(candidates, target, 0, ans, list);

        return ans;
    }
    void combinate(int[] candidates, int target, int start, List<List<Integer>> ans, List<Integer> list) {
        if(target<0) return; //爆了，離開
        if(target==0) { //剛剛好，可以存答案了
            List<Integer> temp = new ArrayList<Integer>(list);
            ans.add(temp);
            return;
        }
        for(int i=start; i<candidates.length; i++) {
            if(target-candidates[i]<0) continue; //爆了，離開
            list.add(candidates[i]);
            combinate(candidates, target-candidates[i], i, ans, list);
            list.remove(list.size()-1);
        }
    }
}
