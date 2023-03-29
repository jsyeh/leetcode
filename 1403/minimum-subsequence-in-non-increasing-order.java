class Solution {
    public List<Integer> minSubsequence(int[] nums) {
        List<Integer> ans = new ArrayList<Integer>();

        int N = nums.length;
        Arrays.sort(nums);
        int [] bigFirst = new int [N]; //從大到小的陣列
        int [] table1 = new int[N]; //sum of first i-elememts) big one
        int [] table2 = new int[N]; //sum i 之後(不含)的元素和

        for(int i=0; i<N; i++){
            bigFirst[i] = nums[N-1-i];

            if(i==0) table1[i] = bigFirst[0];
            if(i>0) table1[i] = table1[i-1]+bigFirst[i];
            //System.out.print(table1[i] + " ");
        }

        //System.out.println();
        table2[N-1] = 0;
        for(int i=N-1-1; i>=0; i--){
            table2[i] = table2[i+1] + bigFirst[i+1];
        }
        
        for(int i=0; i<N; i++){
            //System.out.print(table2[i] + " ");
            if(table1[i]<=table2[i]) {
                ans.add(bigFirst[i]);
                //System.out.print("ahh");
            }else{
                ans.add(bigFirst[i]);
                break;
            }
        }


        return ans;
    }//case 3: [6]
}
