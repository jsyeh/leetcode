class Solution {
    public List<List<Integer>> combine(int n, int k) {
        //recursion
        return combine(1,n,k);
    }
    List<List<Integer>> combine(int start, int n, int k) {
        System.out.println("combine start: " + start);
        System.out.println(" start:" + start);
        System.out.println(" n:" + n);
        System.out.println(" k:" + k);
        List<List<Integer>> ans = new ArrayList<List<Integer>>();
        if(k==0) return ans;
        if(k==1){
            for(int i=start; i<start+n; i++) {
                List<Integer> list = new ArrayList<Integer>();
                list.add(i);
                ans.add(list);
            }
            return ans;
        }
        for(int i=1; i<=n-k+1; i++){
            System.out.println(" line:21 i:" + i);
            List<List<Integer>> listAll = combine(start+i, n-i, k-1);
            for(List<Integer> list : listAll) {
                list.add(0, i+start-1);
                ans.add(list);
            }
        }
        return ans;
    }
}
