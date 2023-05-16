class ParkingSystem {
public:
    int space[4]={};
    ParkingSystem(int big, int medium, int small) {
        space[1] = big;
        space[2] = medium;
        space[3] = small;
    }
    
    bool addCar(int carType) {
        if(space[carType]<=0) return false;
        
        space[carType]--;
        return true;
    }
};

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * ParkingSystem* obj = new ParkingSystem(big, medium, small);
 * bool param_1 = obj->addCar(carType);
 */
