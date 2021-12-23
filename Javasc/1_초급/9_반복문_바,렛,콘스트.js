for ( let i = 0; i < 10; i++){
    // 반복할 코드
}
// ----------------------------
// while 반복문
let i = 0;
while(i < 10){
    console.log(i);
    i++;
}
// 자바에서는 for( int i = 0; i < 10 ; i++){}

// var 는 유연한 변수 선언이 가능
// const는 한번만 변수 선언이 가능
// let 도 유연한 변수 선언이 가능하나 아래와 같은 변수 선언은 불가능하다

let name = 1;
let name = 2; // 에러발생
name = 3; // 가능