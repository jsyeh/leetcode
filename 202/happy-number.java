class Solution {
    public boolean isHappy(int n) {
        HashSet<Integer> set = new HashSet<>();

        while(n!=1){
            if(set.contains(n)){
                return false;
            }
            set.add(n);

            n = sum_square(n);
        }
        return true;
    }
    int sum_square(int n) {
        int ans = 0;
        while(n>0){
            ans += (n%10)*(n%10);
            n = n / 10;
        }
        return ans;
    }
}
