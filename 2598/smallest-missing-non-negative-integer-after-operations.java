class Solution {
    int [] table;
    public int findSmallestInteger(int[] nums, int value) {
      table = new int[value];
      
      //show(nums);
      
      int N = nums.length;
      for(int i=0; i<N; i++){
        int now = nums[i] = nums[i]%value;
        if(now<0){
          now+=value;
          nums[i] = now;
        }
        table[now]++;
      }
      //java.util.Arrays.sort(nums);
      //show(nums);
      
      if(table[0]==0) return 0;

      int ans=0;      
      for(int v=0; v<=N; v++){
        if(table[v%value]>0){
          ans++;
          table[v%value]--;
          if(v==N) ans++;//全部成功的話，再多1個
        }else{
          //ans++;
          break;
        }
      }
      return ans;
    }
}
//Case3:[1,2,3,4,5,6,7,8,9,10]
//7 要得到 11
//Case4: [1,3,5,7]
//2 要得到 0
//Case5: [1,-10,7,13,6,8]
//5 要得到 4

