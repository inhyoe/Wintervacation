var sayNode = function(){
    console.log('node')
}

var es = 'ES';

var oldObject = {
    sayJs: function(){
        console.log('JS');
    },
    sayNode: sayNode
};
oldObject[es+6] = 'Fantastic';

oldObject.sayNode();
oldObject.sayJs();

console.log(oldObject.ES6);