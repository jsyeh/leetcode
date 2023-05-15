/*int comp(const void *p1, const void *p2){
    return *(int*)p1 - *(int*)p2;
}*/
bool checkIfExist(int* arr, int arrSize){
    /*qsort(arr, arrSize, sizeof(int), comp);
    int j=1;
    for(int i=0; i<arrSize && j<arrSize; i++){
        while(j<arrSize && arr[i]*2>arr[j]) j++;
        if(j<arrSize && arr[i]*2==arr[j]) return true;
    }*/
    for(int i=0; i<arrSize; i++){
        for(int j=0; j<arrSize; j++){
            if(i==j) continue;
            if(arr[i]*2==arr[j]) return true;
        }
    }
    return false;
}
//case 106/108: [-10,12,-20,-8,15]
//遇到負的話，原本的想法就錯了
