// var는 함수스코프
// 함수스코프는 만일 함수(function)내에서 선언한 var형 변수를 함수 밖에서 호출할 수 있다는 소리
const age = 30;

if(age > 19){
    var txt = '성인';
}
console.log(txt); // 성인 let, const는 사용 x
//단
const age = 30;
function add(num1,num2){
    var result = num1+num2;
    return result;
}

console.log(result) // error
// let, const는 블록스코프
// 블록스코프는 함수 내에서 선언한 변수는 지역변수라는 뜻.(함수 , if , for ...)