/**
 * @param {Function} fn
 * @return {Function}
 */
var once = function(fn) {
    var used=0;
    return function(...args){
        if(used==0){
            used++;
            var ans = fn(...args); 
            return ans;
        }else return undefined;
    }
};
//這個需求很奇怪, 竟然只讓 function 只能呼叫一次

/**
 * let fn = (a,b,c) => (a + b + c)
 * let onceFn = once(fn)
 *
 * onceFn(1,2,3); // 6
 * onceFn(2,3,6); // returns undefined without calling fn
 */
