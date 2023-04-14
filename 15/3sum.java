class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        int N = nums.length;
        Arrays.sort(nums);

        List<List<Integer>> ans = new ArrayList<List<Integer>>();

        int numI0=Integer.MIN_VALUE, numJ0=Integer.MIN_VALUE;
        for(int i=0; i<N; i++){
            while(i<N && nums[i]==numI0) i++;
            if(i>=N) break;
            numI0 = nums[i];

            for(int j=i+1; j<N; j++){
                while(j<N && nums[j]==numJ0) j++;
                if(j>=N) break;
                numJ0 = nums[j];

                int sum = nums[i]+nums[j];
                int k = Arrays.binarySearch(nums, j+1, N, -sum);
                if(k>=0){
                    ArrayList<Integer> list = new ArrayList<Integer>();
                    list.add(nums[i]);
                    list.add(nums[j]);
                    list.add(nums[k]);
                    ans.add(list);
                }
            }
        }
        return ans;
        //寫到一半,突然有了新的方向
        /*
        HashMap<Integer,List<Integer>> map = new HashMap<Integer,List<Integer>>();
        for(int i=0; i<N; i++){
            for(int j=i+1; j<N; j++){
                int sum = nums[i]+nums[j];
                if(map.containsKey(sum)){
                    List<Integer> list = map.get(sum);
                    list.add(i*N+j);
                }else{
                    ArrayList<Integer> list = new ArrayList<Integer>();
                    list.add(i*N+j);
                    map.put(sum, list);
                }
            }
        }
        for(int k=0; k<N; k++){
            if(map.containsKey(-nums[k])){
                List<Integer> list = map.get(-nums[k]);
                //這裡取出的 list 可能對應的id會重覆
            }
        }
        return ans;*/
    }
}
