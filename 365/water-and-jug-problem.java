class Solution {
    public boolean canMeasureWater(int jug1, int jug2, int total) {
        if(jug1+jug2<total) return false;

        if(jug1==total || jug2==total || jug1+jug2==total) return true;

        return total%gcd(jug1, jug2) == 0;
    }
    int gcd(int a, int b){
        if(a==0) return b;
        if(b==0) return a;
        return gcd(b, a%b);
    }
}
