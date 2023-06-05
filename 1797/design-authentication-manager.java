class AuthenticationManager {
    HashMap<String,Integer> map = new HashMap<>();
    int TTL = 0;
    public AuthenticationManager(int timeToLive) {
        TTL = timeToLive;        
    }
    
    public void generate(String tokenId, int currentTime) {
        map.put(tokenId, currentTime+TTL);        
    }
    
    public void renew(String tokenId, int currentTime) {
        if(map.containsKey(tokenId)) {
            int t = map.get(tokenId);
            if(t>currentTime) map.put(tokenId, currentTime+TTL);
        }        
    }
    
    public int countUnexpiredTokens(int currentTime) {
        int ans = 0;
        for(String tokenId : map.keySet()) {
            if(map.get(tokenId) > currentTime) {
                ans++;
            } else {
                //map.remove(tokenId);
            }
        }
        return ans;    
    }
}

/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager* obj = new AuthenticationManager(timeToLive);
 * obj->generate(tokenId,currentTime);
 * obj->renew(tokenId,currentTime);
 * int param_3 = obj->countUnexpiredTokens(currentTime);
 */
/**
 * Your AuthenticationManager object will be instantiated and called as such:
 * AuthenticationManager obj = new AuthenticationManager(timeToLive);
 * obj.generate(tokenId,currentTime);
 * obj.renew(tokenId,currentTime);
 * int param_3 = obj.countUnexpiredTokens(currentTime);
 */
