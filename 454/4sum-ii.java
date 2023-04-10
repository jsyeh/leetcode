class Solution {
    public int fourSumCount(int[] nums1, int[] nums2, int[] nums3, int[] nums4) {
        int N = nums1.length;
        HashMap<Integer,Integer> map = new HashMap<Integer,Integer>();
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                int sum = nums1[i]+nums2[j];
                if(map.containsKey(sum)){
                    map.put(sum, map.get(sum)+1);
                }else{
                    map.put(sum, 1);
                }
            }
        }
        int ans=0;
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                int sum = nums3[i]+nums4[j];
                if(map.containsKey(-sum)){
                    ans += map.get(-sum);
                }
            }
        }
        return ans;
    }
}
