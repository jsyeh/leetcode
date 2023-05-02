class Solution {
    public List<Integer> findSmallestSetOfVertices(int n, List<List<Integer>> edges) {
        int [] inN = new int[n];
        int [] outN = new int[n];
        for(List<Integer> edge : edges){
            outN[edge.get(0)]++;
            inN[edge.get(1)]++;
        }
        List<Integer> ans = new ArrayList<Integer>();
        for(int i=0; i<n; i++){
            if(inN[i]==0) ans.add(i);
        }
        return ans;
    }
}
