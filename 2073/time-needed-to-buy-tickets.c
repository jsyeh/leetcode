int timeRequiredToBuy(int* tickets, int ticketsSize, int k) {
    int ans = 0;
    for(int i=0; i<=k; i++){
        if(tickets[i]<=tickets[k]) ans += tickets[i];
        else ans += tickets[k];
    }
    for(int i=k+1; i<ticketsSize; i++){
        if(tickets[i]<tickets[k]) ans += tickets[i];
        else ans += tickets[k]-1;
    }
    return ans;
}
