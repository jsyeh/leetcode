class Solution {
    public int minMaxGame(int[] nums) {
        int op = 0; //0:min, 1:max
        int N = nums.length;
        
        while(N>1){
            for(int i=0; i<N; i+=2){
                //System.out.println(N);
                if(op==0){
                    nums[i/2] = min(nums[i], nums[i+1]);
                } else {
                    nums[i/2] = max(nums[i], nums[i+1]);
                }
                //System.out.print(nums[i/2] + " ");
                op = (op+1)%2;
            }
            N/=2;
            //System.out.println();
        }
        return nums[0];
    }
    int min(int a, int b) {
        if(a<b) return a;
        else return b;
    }
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
}//case3: [70,38,21,22]
