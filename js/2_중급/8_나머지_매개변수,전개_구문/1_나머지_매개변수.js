// ...으로 사용

function showName(name){
    console.log(name);
}// 개수가 제한이 없음.
showName('Mike')
showName('Mike','Tom') // 첫번째 인자가 접근
showName(); // undenfined

// argument란?

// 함수로 넘어 온 모든 인수(인자)에 접근
// 함수내에서 이용 가능한 지역 변수
// length/index
// Array 형태의  ************
// 배열의 내장 메서드 없음 (forEach,map)

console.log('=========argument사용=========')
function showName(name){
    console.log(arguments.length);
    console.log(arguments[0]);
    console.log(arguments[1]);
}

showName('Mike','Tom');

// ***** 나머지 매개변수 *****
console.log('***** 나머지 매개변수 *****')
function showName(...names){
    console.log(names) //names는 배열 이름
}
showName()
showName('Mike')
showName('Mike','Tom')

// function add(...numbers){
//     let result = 0;
//     numbers.forEach(function(num){
//         result += num;
//     });
//     console.log(result)
// } // argument와는 다르게 메서드 사용 가능
function add(...numbers){
    let result = numbers.reduce((prev,cur) =>{
        return prev + cur
    },0)
    console.log(result)
}
add(1,2,3)
function add(...numbers){
    let result = numbers.reduce((prev,cur) =>prev+cur)
    console.log(result)
}
// var result = userList.reduce((prev,cur)=>{
//     return prev = Number(prev)+Number(cur.age)
// },0);


add(1,2,3);
add(1,2,3,4,5,6,7,8,9,10)

// 나머지 매개변수
// user 객체를 만들어 주는 생성자 함수를 만들다.

function User(name,age,...skill){
    this.name = name;
    this.age = age;
    this.skill = skill;

}

var user1 = new User('Mike',30,'html','css')
var user2 = new User('Tom',32,'Js','React')
console.log(user1)
console.log(user2)
