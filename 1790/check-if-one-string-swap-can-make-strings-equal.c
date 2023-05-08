bool areAlmostEqual(char * s1, char * s2){
    int N = strlen(s1);

    int diff1=0, diff2=0, diffN=0;
    for(int i=0; i<N; i++){
        if(s1[i]!=s2[i]){
            diffN++;
            diff2 = diff1;
            diff1 = i;
        }
    }
    if(diffN==0) return true;
    if(diffN==2 && s1[diff1]==s2[diff2] && s1[diff2]==s2[diff1]) return true;
    else return false;
}
