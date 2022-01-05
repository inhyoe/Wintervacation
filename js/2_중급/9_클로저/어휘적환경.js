var one;
one = 1;


function addOne(num){
    console.log(one + num)
}
addOne(5)

function makeAdder(x){
    return function(y){
        return x + y;
    }
}

var add3 = makeAdder(3); // x 값에 3이 들어가고 3 fucntion(y){return 3+y} 가 리턴됨
console.log(add3(2))     // y 값에 2가 들어가고 5값이 출력됨 
// add 3 함수가 생성된 이후에도 상위함수인 makeAdder의 x에 접근이 가능하다.
// 이 기능을 클로저 라고 한다.

var add10 = makeAdder(10);
console.log(add10(5)) 
console.log(add3(1))