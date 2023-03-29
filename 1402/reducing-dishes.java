class Solution {
    public int maxSatisfaction(int[] satisfaction) {
        Arrays.sort(satisfaction);
        int N = satisfaction.length;
        int [] bigFirst = new int[N];
        int [] table = new int[N];
        for(int i=0; i<N; i++){
            bigFirst[i] = satisfaction[N-1-i];
        }
        table[0] = bigFirst[0];
        for(int i=1; i<N; i++){
            table[i] = table[i-1]+bigFirst[i];
        }

        int max = 0, now=0;
        for(int i=0; i<N; i++){
            if(table[i]+now>max) max = table[i]+now;
            now += table[i];
        }
        return max;
    }
}
