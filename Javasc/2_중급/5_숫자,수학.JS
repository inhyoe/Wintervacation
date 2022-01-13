// thString()  10진수 -> 2진수 / 16진수

let num = 10;
num.toString(); // 10진수
num.toString(2); // 1010
let num1 = 255;
num1.toString(16); // ff

Math.PI; // 원주율

// 수학 매소드

let num2 = 5.1;
let num3 = 5.7;
// ===========올림(Math.ceil())==============

Math.ceil(num2); // 6
Math.ceil(num3); // 6

// ===========내림(Math.floor())==============

Math.ceil(num2) // 5
Math.ceil(num3) // 5

// ===========반올림(Math.round())==============

Math.round(num2) // 5
Math.round(num3) // 6

// ===========소숫점 자릿수(toFixed())==============
// 요구사항 소수점 둘째자리까지 표현하시오.
let userRate = 30.1234
Math.round(userRate*100)/100 // 30.12

userRate.toFixed(2); // 30.12
userRate.toFixed(0); // 30 정수부.
userRate.toFixed(6); // 30.123400
//단 toFixed 메소드는 String형을 반환한다.
// 그러므로 수식처리를 할떄는 Number형으로 바꿔준다.

// ===========Nan인지 반환해줌(isNaN())==============

let x = Number('x'); //NaN (Not a Number)
x == NaN // false
x === NaN // false
NaN == NaN // false
// 그러므로 isNaN만이 NaN인지 판별해줌.
// ex)
isNaN(x) // True
isNaN(3) // false

// ===========문자열을 숫자로 반환해줌(paeseInt())==============
let margin = '10px'
parseInt(margin) // 10
Number(margin) // NaN

console.log(parseInt('f3')); //NaN
console.log(parseInt('3f4'));  //3
// parseInt는 문자열이 만나기 전 숫자까지만 반환해준다
// parseInt의 두번째 인자값을 해당하는 진수값으로 반환해준다.
let redColor = 'f3';
parseInt(redColor) // NaN
parseInt(redColor,16) // 243
parseInt('11',2) // 3

// ===========문자열을 숫자로 반환해주며 부동소수점(paeseFloat())==============
let padding = '18.5%';
parseInt(padding) // 18
parseFloat(padding) //18.5

// ===========랜덤한 0<x<1이하의 소수를 반환함(Math.random())==============
Math.random() // 0.xxxxx
//1 ~ 100 사이의 임의의 숫자를 뽑고싶다면
Math.floor(Math.random()*100) +1

// ===========최댓값, 최솟값을 반환함(Math.max()/Math.min())==============
Math.max(1,4,-1,5,10,9,5.54) // 10
Math.min(1,4,-1,5,10,9,5.54) // -1

// ===========절댓값을 반환함 (Math.abs())==============

Math.abs(-1) // 1

// ===========거듭제곱값 Math.pow(n,m)==============
Math.pow(3,2) // 3**2

// ===========제곱근 Math.sqrt(n)==============
Math.sqrt(16) // 4
