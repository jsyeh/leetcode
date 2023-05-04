char * predictPartyVictory(char * senate){
    int banR=0, banD=0, aliveR=0, aliveD=0;
    char now;
    for(int i=0; senate[i]!=0; i++){
        if(senate[i]=='R') aliveR++;
        else aliveD++;
    }

    do{
        int pos=0;
        for(int i=0; senate[i]!=0; i++){
            now = senate[i];
            if(now=='R'){
                if(banR>0){ //前人下了 ban指令,讓你死
                    banR--; 
                    aliveR--;
                    senate[i] = 'X';
                }else{ //沒任何人ban你,你可以ban別人
                    banD++;
                }
            }else if(now=='D'){
                if(banD>0){
                    banD--;
                    aliveD--;
                    senate[i] = 'X';
                }
                else {
                    banR++;
                }
            }
            if(aliveR>0 && aliveD==0) return "Radiant";
            if(aliveD>0 && aliveR==0) return "Dire";
        }
    }while(aliveR>0 && aliveD>0);
    return "Dire";
}//case 76/82: "DDRRR"
//"DRRDRDRDRDDRDRDR"
