// 형변환이 필요한 이유
const mathscore  = prompt('수학 몇점?');
const engscore  = prompt('영어 몇점?');
const result = (mathscore + engscore) / 2 ;
console.log(result)
// 이 결과는 잘못됨
// 왜냐하면 String형을 더했기 때문이다
// 그러므로 '9080' = 4540 이 출력됨
// 개선하려면
const mathscore  = Number(prompt('수학 몇점?'));
const engscore  = Number(prompt('영어 몇점?'));
const result = (mathscore + engscore) / 2 ;
console.log(result)

// ------------- 형변환
console.log(
    String(3),
    String(true),
    String(false),
    String(null),
    String(undefined)
)
console.log(
    Number(3),  // 3 
    Number(true), // 1
    Number(false),  // 2
    Number('3asdasda'), // Nan
    String(null),
    Number(undefined)
)
number(null) // 0
number(undefined) // NaN

// boolean형
// 숫자 0 , 빈문자열 '' , null , undefined , NaN 외에는 모두 true를 반환한다.