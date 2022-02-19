// var와 let의 차이점

var name1 = 'mike';
var name2 = 'siri'; // 선언이 다시 되어도 재선언 가능.

let kane = 'kane';
let kane2 = 'kane'; // error

//var는 호이스팅으로 선언 전에 사용이 가능하다. 다만 name이라는 변수만 호이스팅되고 값은 호이스팅되지 않음

// ex

var name3;
console.log(name3); // undefined
name3 = 'mike'

let name1;
console.log(name1); // error // TDG (Temporal Dead Zone) 호이스팅되나 호출 x되며 TDG로인해 x
name1 = 'mike'

//변수의 생성 과정
// 선언단계
// 초기화단계
// 할당단계 command /

// 1 var는 선언과 초기화가 동시에됨.
// 2 할당단계

// let은 1.선언 -> 2.초기화 -> 3.할당

// const는 선언,초기화,할당이 동시에 되어야함.

// ex) let age gender.
let name4;
name4 = mike;

var age4;
age4 = 30;

const gender5; // error
gender5 = 'male'; // Error 선언만하고 초기화, 할당이 따로되었기 때문이다.

