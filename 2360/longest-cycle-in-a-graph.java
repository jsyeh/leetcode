class Solution {
    public int longestCycle(int[] edges) {
        //偷看 Discussion 裡，有人再次介紹 fast/slow 測試cycle方法
        int ans = -1;
        boolean [] visited = new boolean[edges.length];
        for(int i=0; i<edges.length; i++){
            if(visited[i]) continue;

            int fast=i, slow=i;
            while(true) {
                fast = edges[fast];
                if(fast==-1 || edges[fast]==-1) break;                
                fast = edges[fast];

                slow = edges[slow];
                if(visited[slow]) break;
                visited[slow]=true;

                if(slow==fast){ //找到 cycle了，判斷長度
                    int len=0;
                    while(true){
                        fast = edges[edges[fast]];
                        slow = edges[slow];
                        len++;
                        if(slow==fast) break;
                    }
                    if(len>ans) ans = len;
                    break;
                }
            }

        }
        return ans;
    }
}//case3: [1,2,0,4,5,6,3,8,9,7]
//case4: [59,83,46,18,45,52,-1,-1,46,-1,75,86,89,-1,-1,-1,-1,7,-1,34,-1,-1,-1,34,82,-1,75,30,34,-1,87,7,35,-1,-1,54,72,-1,-1,-1,29,56,-1,55,32,44,62,-1,80,-1,-1,15,81,-1,32,-1,-1,53,81,40,81,72,68,-1,-1,-1,87,73,-1,-1,55,-1,-1,-1,-1,-1,53,89,38,25,16,4,71,7,33,-1,42,34,29,33,1,23,-1]
