let student = ['철수','영희','영수']
//              0      1    2  의 인덱스 번호를 가지고 있다.
// 인덱스 수정 방법
student[0] = '진정' // student[0]이 진정으로 변함

//배열은 숫자, 객체,함수 등도 포함가능

let arr = [
    '민수', 3,false,
    {
        name : '민수',
        age : 30,
    },
    function(){
        console.log('Test')
    }
] // Object, fucntion또한 한개로 취급 .

// 배열의 길이
student.length // 30

// 메소드
let days = ['월','화','수']
days.push('목') // 제일 뒤에 추가
days.pop() // 제일 뒤의 요소를 삭제
days.unshift('일') // 요소 제일 앞에 추가
days.shift() // 제일 앞의 요소를 삭제

//반복문 for in for i for of
let days = ['월','화','수']
for ( let day of days){ // for in 과 같지만 for of를 사용
    console.log(day)
}