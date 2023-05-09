/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    let newArr = [];
    for(let i = 0; i<arr.length; i++){
        let temp = fn(arr[i], i);
        if(temp) newArr.push(arr[i]);
    }
    return newArr;
};
