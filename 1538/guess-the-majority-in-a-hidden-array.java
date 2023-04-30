/**
 * // This is the ArrayReader's API interface.
 * // You should not implement it, or speculate about its implementation
 * interface ArrayReader {
 *   public:
 *     // Compares 4 different elements in the array
 *     // return 4 if the values of the 4 elements are the same (0 or 1).
 *     // return 2 if three elements have a value equal to 0 and one element has value equal to 1 or vice versa.
 *     // return 0 : if two element have a value equal to 0 and two elements have a value equal to 1.
 *     public int query(int a, int b, int c, int d);
 *
 *     // Returns the length of the array
 *     public int length();
 * };
 */

class Solution {
    public int guessMajority(ArrayReader reader) {
        int N = reader.length();
        int [] query = new int[N]; //query對照表，用來比對與a[0]是否相同
        boolean [] same = new boolean[N]; //確認是否與a[0]相同

        //能不能從 query 把每個答案找出來? query數字的意思是 2群差多少
        //所以若有4 則代表大家都同一國，很好
        //但若都沒有4就慘了
        //===以下的思考都沒有用，請省略
        //假設 a[0] = 0; query(0,1,2,3) 
        //規則：map如果都是0,要看N是奇數(奇數筆) or 偶數(-1無法判斷)
        //規則：只要有4，就有辦法推算出全部的值，因為可用3個去掃出另外1個的值
        //規則：若有2，就是3打1，有辦法推出4的組合嗎？
        //===以上的思考都沒有，請省略
        query[0] = reader.query(0,1,2,3); 
        same[0] = true;
        int vote0=1;//本來0就要投自己1票
        int other=0;
        //System.out.print("[0]:" + query[0] + " [4]:");
        for(int i=4; i<N; i++){
            query[i] = reader.query(1,2,3,i);
            if(query[0] == query[i]){
                same[i] = true; //與 a[0]相同   
                vote0++;
            }else other = i;
            //System.out.print(query[i] + " "); //印出的對照表
        }
        //太少的話，不好查看。如果n>=6，就可有3個去夾擊3人
        //n:5 不好處理，但還是可查出來，因使用2次查詢來夾擊
        if(N>=7){
            for(int i=1; i<=3; i++){ //把不知道的2,3,4都找出來
                int Q = reader.query(0,i,5,6); //query的結果
                same[i] = testSame(true, same[5], same[6], Q);
                if(same[i] == true) vote0++;
                else other = i;
            }
        } else if(N==5 || N==6){
            int Q10 = reader.query(0,2,3,4);
            int Q11 = reader.query(1,2,3,4);
            if(Q10==Q11) same[1]=true;
            else same[1] = false;
            int Q20 = reader.query(0,1,3,4);
            int Q22 = reader.query(1,2,3,4);
            if(Q20==Q22) same[2]=true;
            else same[2] = false;
            if(N==6){
                int Q30 = reader.query(0,1,4,5);
                int Q33 = reader.query(1,3,4,5);
                if(Q30==Q33) same[3]=true;
                else same[3] = false;
            }
        }

        int voteSame=0, voteOther=0, indexSame=0, indexOther=0;
        for(int i=0; i<N; i++){
System.out.print(same[i] + " ");
            if(same[i]==true){
                voteSame++;
                indexSame = i;
            }else {
                voteOther++;
                indexOther = i;
            }
        }
System.out.println("voteSame:" + voteSame);
        if(voteSame>voteOther) return indexSame;
        else if(voteOther>voteSame) return indexOther;
        else return -1;
//System.out.println(vote0);
//        if(vote0>N/2) return 0; //投a[0]一票的人比較多
//        else if(vote0<N/2) return other; //投另外其他的人
//        else return -1;
    }
    boolean testSame(boolean a, boolean c, boolean d, int query) {
        if(c==true && d==true && query==2) return false;
        else if(c==true && d==true && query==4) return true;
        else if( (c^d) && query==0) return false;
        else if( (c^d) && query==2) return true;
        else if(c==false && d==false && query==2) return false;
        else return true ;//if(c==false && d==false && query==0) return true;
        // true ?? true true 可得到 2 or 4
        // true ?? true false 可得到 0 or 2
        // true ?? false false 可得到 2 or 0
    }
}//case 6/135: [0,0,0,0,1]
//case 7/135: [0,0,1,1,0,1]
//case 112/135: [1,1,0,1,1,0,1,0,0,0]
