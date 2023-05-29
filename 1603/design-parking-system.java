class ParkingSystem {
    int [] a = new int[4];
    int [] b = new int[4];
    public ParkingSystem(int big, int medium, int small) {
        a[1] = big;
        a[2] = medium;
        a[3] = small;
    }
    
    public boolean addCar(int carType) {
        if(b[carType] < a[carType]){
            b[carType]++;
            return true;
        }else return false;
    }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem obj = new ParkingSystem(big, medium, small);
 * boolean param_1 = obj.addCar(carType);
 */
