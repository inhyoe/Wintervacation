// hoisting 함수가 호출순위 위에 선언되어도 실행됨 (호이스팅)

x()
function x(){
    console.log('Hello');

} // 호이스팅

// 함수표현식 = 코드에 도달하면 생성돤다 아래의 예제를 보자

let sayHello = function(){
    console.log('Hello');
}
sayHello(); // 함수 표현식

// 화살표 함수 (arrow function)
let add = function(num1,num2){
    return num1+num2;
}
// 를
let add =(num1,num2) => (
    num1 + num2
)
let add = (num1,num2) => num1+num2

// 예제
showError()
function showError(){
    console.log('error');
}
// 화살표 함수

let Error = () =>{
    console.log('error');
}
Error()

// 예제2
const sayHello = function(name){
    const msg = `Hello, ${name}`;
    console.log(msg);
}
sayHello();

const sayHello = (name)=> {
    const msg = `Hello, ${name}`;
    console.log(msg)
}

// 화살표 함수

const sayHello = (name) =>{
    const msg = `Hello, ${name}`;
    console.log(msg);
}
sayHello();

// 예제3
const add = function(num1,num2){
    return num1+num2;
}

add()

//화살표 함수
const add = (num1,num2) => (  num1+num2  );
