class Solution {
    public int countQuadruplets(int[] nums) {
        int N = nums.length;
        
        //Arrays.sort(nums); 題目不能亂排序
        for(int i=0; i<N; i++) System.out.print(nums[i] + " ");
        int ans=0;
        for(int i=0; i<N; i++) {
            for(int j=i+1; j<N; j++) {
                for(int k=j+1; k<N; k++) {
                    for(int a=k+1; a<N; a++){
                        if(nums[i]+nums[j]+nums[k]==nums[a]){
                            ans++;
                            System.out.println(nums[i] + " " + nums[j] + " " + nums[k] + " " + nums[a]);
                        }
                    }
                    /*int sum = nums[i] + nums[j] + nums[k];
                    int next = k;
                    System.out.println(next);
                    while(next>=0){
                        next = Arrays.binarySearch(nums, next+1, N, sum);
                        System.out.print(next);
                        if(next>=0) ans++;
                    }*/
                }
            }
        }
        return ans;
    }
}
//case4: [9,6,8,23,39,23]
//排序後是 [6,8,9,23,23,39] (糟,不可以排序)
//因6+8+9=23,有出現2次,所以有技巧把它找出來
//case5: [28,8,49,85,37,90,20,8]
//排序後是 8 8 20 28 37 49 85 90 (糟,不可以排序)
//我以為是 8 28 49 85
//8 28 49 85
//20 28 37 85 共3組,但答案只有1組
