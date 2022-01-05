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

var arr = [3, 4, 5];

    for (var i = 0; i < arr.length; i++) { // 배열 arr의 모든 요소의 인덱스(index)를 출력함.
      document.write(arr[i] + " ");
    }
    document.write("<br>");
    

    for (var value of arr) { // 위와 같은 동작을 하는 for / of 문
      document.write(value + " ");
    }


//forEach반복문 
const arr = [0,1,2,3,4,5,6,7,8,9,10];

    arr.forEach(function(element){
        console.log(element); // 0 1 2 3 4 5 6 7 8 9 10
    });
    // 혹은 arrow 함수 가능
    arr.forEach(element => console.log(element));