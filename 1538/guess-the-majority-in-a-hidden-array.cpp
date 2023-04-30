class Solution {
public:
    int guessMajority(ArrayReader &reader) {
        // Idea: Keep/Maintain 3 Points of Contact, only 1 Point Move
        // The Idea is used in "Ladder Safety" and "Climbing Safety"
        // - "3 Points Of Contact Rule Of Ladder Safety"
        // - "Maintain Three Points of Contact for Climbing Safety"

        int N = reader.length(); //array lengh of a[i]
        bool same[N]; 
        // same[i] means "a[0] and a[i] are the same"

        // The Idea is to test all a[i] if they are the same as a[0]
        // if(a[0] == a[i]) same[i] = true;
        // else same[i] = false;

        // However, you can't find the Invisible a[i].
        // Therefore, you can use query() to do the similar thing.

        // ex. int Q0 = reader.query(0, 2,3,4);
        //     int Q1 = reader.query(1, 2,3,4) ;
        // if(Q0 == Q1) same[1] = true; //a[0] and a[1] are the same
        // else same[1] = false;    //a[0] and a[1] are not the same

        // In short, you can write: same[1] = (Q0 == Q1);
        
        // Careful: query(a,b,c,d) where a<b<c<d 
        // So you can't use query(0,0,0,0) vs. query(0,0,0,i) 

        //=======
        //Part 1: The first 5 elements (combination -- not easy)

        // For the first 5 elements (0, 1,2,3,4)
        same[0] = true; //of course, a[0] equals a[0], the same

        // Find same[1], same[2], same[3], same[4]
        // 1,2,3,4 are your choices
        // if you want to find 1, keep/maintain 2,3,4
        // if you want to find 2, keep/maintain 1,3,4
        // if you want to find 3, keep/maintain 1,2,4
        // (same[4] can easily be found in Part 2)

        int Q10 = reader.query(0,  2,3,4);
        int Q11 = reader.query(  1,2,3,4);
        same[1] = (Q10==Q11); //maintain 2,3,4 => find 1

        int Q20 = reader.query(0,1,  3,4);
        int Q22 = reader.query(  1,2,3,4);
        same[2] = (Q20==Q22); //maintain 1,3,4 => find 2

        int Q30 = reader.query(0,1,2,  4); 
        int Q33 = reader.query(  1,2,3,4);
        same[3] = (Q30==Q33); //maintain 1,2,4 => find 3

        //=======
        //Part 2: The others (use for loop -- easy)
        // Idea: Keep/Maintain 1,2,3, find i: 4,5,6...
        // int Q0 = reader.query(0, 1,2,3);
        // same[4] =  (reader.query(1,2,3, 4) == Q0); //4 vs. 0
        // same[5] =  (reader.query(1,2,3, 5) == Q0); //5 vs. 0
        // ...
        // same[i] =  (reader.query(1,2,3, i) == Q0); //i vs. 0

        int Q0 = reader.query(0, 1,2,3); 
        for(int i=4; i<N; i++){
            same[i] = (reader.query(1,2,3, i) == Q0);
        }

        //Finally, vote/count same[i] 
        int voteSame=0, voteOther=0;
        int indexSame=0, indexOther=0; //index will be return latter
        for(int i=0; i<N; i++){
            if(same[i]==true){
                voteSame++; //a[i] & a[0] are the same. vote Same
                //indexSame = i; //not necessary. you can return 0 directly
            }else {
                voteOther++; //a[i] & a[0] are not the same, vote Other
                indexOther = i; //remember the index of the other
            }
        }
        if(voteSame>voteOther) return 0; //a[0] win, return 0
        else if(voteOther>voteSame) return indexOther;//the others win
        else return -1; //if the votes of two groups equal, return -1
    }
};
