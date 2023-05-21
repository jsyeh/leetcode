/**
 * @param {Function} fn
 */
function memoize(fn) {
    const cache = {};
    return function() {
        let key = '';
        for(let arg of arguments){
            key += ',' + arg;
        }
        if(key in cache){
            return cache[key];
        }
        let ans = fn(...arguments);
        cache[key] = ans;
        return ans;
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
