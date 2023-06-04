typedef struct {
    int min, val;
} MinStack;

MinStack* stack;
int N;
MinStack* minStackCreate() {
    stack = (MinStack*) malloc(sizeof(MinStack)*30000);
    //因最多叫3*10^4次
    N = 0;
    return stack;
}

void minStackPush(MinStack* obj, int val) {
    if(N==0) stack[N].min = val;
    else stack[N].min = (stack[N-1].min < val)? stack[N-1].min : val;
    stack[N].val = val;
    N++;
}

void minStackPop(MinStack* obj) {
    N--;
}

int minStackTop(MinStack* obj) {
    return stack[N-1].val;
}

int minStackGetMin(MinStack* obj) {
    return stack[N-1].min;
}

void minStackFree(MinStack* obj) {
    free(stack);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * MinStack* obj = minStackCreate();
 * minStackPush(obj, val);
 
 * minStackPop(obj);
 
 * int param_3 = minStackTop(obj);
 
 * int param_4 = minStackGetMin(obj);
 
 * minStackFree(obj);
*/
