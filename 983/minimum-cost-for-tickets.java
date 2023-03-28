class Solution {
    int min(int a, int b, int c) {
        if(a<=b && a<=c) return a;
        if(b<=a && b<=c) return b;
        if(c<=a && c<=b) return c;
        return 0;
    }
    int [] table;
    boolean [] travel;
    public int mincostTickets(int[] days, int[] costs) {
        int [] table = new int[366];
        boolean [] travel = new boolean[366];
        for(int i=0; i<days.length; i++){
            travel[days[i]]=true;
        }
        table[0] = 0;
        for(int i=1; i<366; i++){
            if(travel[i]){
                int a = table[i-1];
                int b = (i<7)? table[0]:table[i-7];
                int c = (i<30)? table[0]:table[i-30];
                table[i] = min(a+costs[0], b+costs[1], c+costs[2]);
            }else table[i] = table[i-1];
        }
        return table[365];
    }
/*        int [] back = {1, 7, 30};
        int [][] table = new int[3][366];
        boolean [] travel = new boolean[366];
        for(int i=0; i<days.length; i++){
            travel[days[i]]=true;
        }
        table[0][0] = 0;
        table[1][0] = 0;
        table[2][0] = 0;
        for(int i=1; i<366; i++){ //1-day only 
            if(travel[i]) table[0][i] = table[0][i-1]+costs[0];
            else table[0][i] = table[0][i-1];
        }

        for(int i=1; i<366; i++){ //plus 7-day
            if(i<7){
                if(travel[i]){
                    table[1][i] = min(table[0][i], table[1][0]+costs[1]);
                } else {
                    table[1][i] = table[1][i-1];
                }
            }else{
                if(travel[i]){
                    table[1][i] = min(table[0][i], table[1][i-7]+costs[1]);
                } else {
                    table[1][i] = table[1][i-1];
                }
            }
        }

        for(int i=1; i<366; i++){ //plus 30-day
            if(i<30){
                if(travel[i]){
                    table[2][i] = min(table[1][i], table[2][0]+costs[2]);
                } else {
                    table[2][i] = table[2][i-1];
                }
            }else{
                if(travel[i]){
                    table[2][i] = min(table[1][i], table[2][i-30]+costs[2]);
                } else {
                    table[2][i] = table[2][i-1];
                }
            }
        }
        return table[2][365];
    }
    int min(int a, int b) {
        if(a<b) return a;
        else return b;
    }*/

}

/*
void setup(){
  int [] days = {1,4,6,7,8,20};
  int [] costs = {2,7,15};
  Solution sol = new Solution();
  int ans = sol.mincostTickets(days, costs);
  //println(ans);
}
*/
