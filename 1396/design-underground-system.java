class CheckIn {
    int ID;
    String name;
    int t;
    CheckIn(int _ID, String _name, int _t){
        ID = _ID;
        name = _name;
        t = _t;
    }
}
class UndergroundSystem {
    HashMap<String, Integer[]> time = new HashMap<>();
    //兩個字串(start,end)車站名, (總秒數,人數), 以方便算出平均時間
    HashMap<Integer,CheckIn> record = new HashMap<>();
    public UndergroundSystem() {
        
    }
    
    public void checkIn(int id, String stationName, int t) {
        record.put(id, new CheckIn(id,stationName,t));
    }
    
    public void checkOut(int id, String stationName, int t) {
        CheckIn one = record.get(id);
        String route = one.name + " " + stationName;
        //if(one.name.compareTo(stationName)>0) route = stationName + " " + one.name;
System.out.println("checkOut: " + route);

        if(time.containsKey(route)){
            Integer[] dt = time.get(route); //dt[0] 是 sum, dt[1] 是 資料數N
            dt[0] += (t - one.t); //sum
            dt[1] ++; //資料數N
            time.put(route, dt);
System.out.println(dt[0] + " " + dt[1]);
        }else{
            Integer[] dt = {t-one.t, 1};
            time.put(route, dt);
System.out.println(dt[0] + " " + dt[1]);
        }
    }
    
    public double getAverageTime(String startStation, String endStation) {
        String route = startStation + " " + endStation;
        //if(startStation.compareTo(endStation)>0) route = endStation + " " + startStation;
System.out.println("getAverageTime: " + route);
        if(time.containsKey(route)) {
            Integer [] dt = time.get(route);
System.out.println(dt[0] + " " + dt[1]);
            return dt[0] / (double) dt[1];
        } else return 0;
    }
}//題目說: The average time is computed from all the previous traveling times from startStation to endStation that happened directly, meaning a check in at startStation followed by a check out from endStation.
//所以不用幫它們交換名字
//case 55/56: ["UndergroundSystem","checkIn","checkIn","checkOut","checkOut","checkIn","checkIn","getAverageTime","getAverageTime","checkOut","getAverageTime","checkOut","getAverageTime"]
//[[],[1,"Leeds",3],[2,"York",8],[1,"York",10],[2,"Leeds",15],[1,"York",20],[2,"Leeds",22],["Leeds","York"],["York","Leeds"],[1,"Leeds",24],["York","Leeds"],[2,"York",38],["Leeds","York"]]

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * UndergroundSystem obj = new UndergroundSystem();
 * obj.checkIn(id,stationName,t);
 * obj.checkOut(id,stationName,t);
 * double param_3 = obj.getAverageTime(startStation,endStation);
 */
