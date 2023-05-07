class Solution {
    public boolean isPerfectSquare(int num) {
        //其實是要確認開根號的值，再平方即可
        int ans = (int)Math.sqrt(num);
        if(ans*ans==num) return true;
        return false;
    }
}
