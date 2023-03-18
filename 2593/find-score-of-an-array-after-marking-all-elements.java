class Num implements Comparable<Num> {
    int val;
    int i;//0-index
    Num(int _val, int _i){
        val = _val;
        i = _i;
    }
@Override
    public int compareTo(Num n2) {
        //let's sort the employee based on an id in ascending order
        //returns a negative integer, zero, or a positive integer as this employee id
        //is less than, equal to, or greater than the specified object.
        return (this.val - n2.val);
    }
    
}
class Solution {
    int [] used; //used[i] 1-index vs. nums[i-1] 0-index
    Num [] all;//0-index
    public long findScore(int[] nums) {
        int N = nums.length;
        used=new int[N+2];
        all=new Num[N];
        for(int i=0; i<N; i++){
            all[i] = new Num(nums[i], i);
        }
        Arrays.sort(all);
        
        long ans=0; //long is important!
        while(true){
            int ii = findSmallest(nums);
            if(ii==-1)break;
            ans += nums[ii-1];
            used[ii]=1;
            used[ii-1]=1;
            used[ii+1]=1;
        }
        return ans;
    }
    int smallest=0; //0-index
    int findSmallest(int[] nums) { //return 1-index
        int N = nums.length;
        for(int i=smallest; i<N; i++){
            int ii = all[i].i;
            if(used[ii+1]==0){
                smallest = i+1;
                return all[i].i+1;
            }
        }
        return -1;
        /*
        int ans = -1, min=0;;
        int N = nums.length;
        //會超時，所以這裡需要資料結構，讓找最小值變快
        for(int i=1; i<=N; i++){
            if(used[i]==0 && ans==-1) {
                ans = i;
                min = nums[i-1];
                continue;
            }
            if(used[i]==0 && nums[i-1]<min){
                ans = i;
                min = nums[i-1];
            }
        }
        return ans;*/
    }
}
