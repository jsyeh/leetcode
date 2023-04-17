class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        int N = candies.length;
        List<Boolean> ans = new ArrayList<Boolean>();
        int max=0;
        for(int i=0; i<N; i++){
            if(candies[i]>max) max=candies[i];
        }

        for(int i=0; i<N; i++){
            if(candies[i]+extraCandies>=max) ans.add(true);
            else ans.add(false);
        }
        return ans;
    }
}
