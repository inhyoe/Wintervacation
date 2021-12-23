// 함수 작성

/* function 변수명(매개변수){
    alert('에러가 발생하였습니다 다시 시도해 주세요.');
} 
showError()*/

//매개변수가 있는 함수


function sayHello(name){
    const msg = `Hello ${name}`;
    console.log(msg)
}
sayHello('Mike');


// 만일 이름을 입력하지 않아서 이름이 없을 경우에는 어떻게 하나?
function sayHello(name){
    let msg = `Hello`; //console에서 let으로 바뀐 이유는 아래에서 msg의 내용이 바뀔 수 있기 때문이다.
    if(name){
        msg = `Hello. ${name}`;
    }
    console.log(msg)
}
sayHello();
console.log(msg)// 그리고 msg는 지역변수라 함수 내에서만 시용이 가능하다 Error출력 !
// name에 아무것도 입력하지 않았기때문에 undefined가 출력이 되며
// hello에는 아무것도 이 출력이 된다


let msg = 'Hello'; // 전역변수 (global varable)
console.log('함수 호출 전')
console.log(msg)

function sayHello(name){
    msg += `, ${name}.`; // 함수 내부에서 msg라는 변수값을 바꿨음. 만일 const라면 변하지 않음. 
    console.log('함수 내부'); // local varable
    console.log(msg);
}

sayHello('Mike');
console.log('함수 호출 후')
console.log(msg);

let msg = 'Welcome'; // 전역변수 
console.log(msg)
function sayHello(name){
    let msg = 'Hello' // 지역변수
    console.log(msg);
}
sayHello('Mike') // 전역변수
console.log(msg)

let name = "Mike";

function sayHello(name){
    console.log(name)
}
sayHello() // undefined
sayHello('Jane') // Jane

function sayHello(name){
    let newName = name || 'friend';
    let msg = `Hello, ${newName}`;
    console.log(msg)
}

sayHello()        // friend 출력
                  // undefined = false 이므로 or 인 friend가 출력되고
sayHello('Jane')  // Jane 출력 // name이 있으므로 Jane 출력

function sayHello(name = 'friend'){
    let msg = `Hello, ${newName}`;
    console.log(msg)
}

sayHello()        // default값을 주어도 된다(name이 없을때)
sayHello('Jane')  // 


