/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let counter = init;
    let backup = init;
    return {
        increment : function(){
            counter++;
            return counter;
        },
        reset : function(){
            counter = backup;
            return backup;
        },
        decrement : function(){
            counter--;
            return counter;
        }
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */
