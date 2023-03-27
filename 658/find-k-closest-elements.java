class Solution {
    public List<Integer> findClosestElements(int[] arr, int k, int x) {
        List<Integer> ans = new ArrayList<Integer>(k);
        int N = arr.length;
        int [] diff = new int[N];
        for(int i=0; i<N; i++){
            diff[i] = abs(arr[i]-x);
        }
        int best=0;
        int sum=0;
        for(int i=0; i<k; i++){
            sum += diff[i];
        }
        for(int i=1; i<=N-k; i++){
            int now = -diff[i-1]+diff[k-1+i];
            if(now<0) best = i;
        }
        /*
        int md0 = abs(arr[0]-x); //min d0
        int md1 = abs(arr[k-1]-x); //min d1
        int md = max(md0, md1);
        int mmd = min(md0, md1);
        int best = 0;
        for(int i=1; i<=N-k; i++){
            int d0 = abs(arr[i]-x);
            int d1 = abs(arr[k-1+i]-x);
            if(max(d0,d1)<md || max(d0,d1)==md && min(d0,d1)<mmd){//這裡要想清楚
                md0 = d0; md1 = d1;
                md = max(md0, md1);
                mmd = min(md0, md1);
                best = i;
            }
        }
        */
        for(int i=0; i<k; i++){
            ans.add(i, arr[i+best]);
        }
        return ans;
    }
    int abs(int n) {
        if(n<0) return -n;
        return n;
    }
    int max(int a, int b) {
        if(a>b) return a;
        else return b;
    }
    int min(int a, int b) {
        if(a<b) return a;
        else return b;
    }
}//case 4: [0,1,2,2,2,3,6,8,8,9] 5 9
//case 5: [1,1,2,2,2,2,2,3,3] 3 3
