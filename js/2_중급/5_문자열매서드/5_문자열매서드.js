// 백틱은 여러줄을 포함 할 수 있다

let desc = `여러줄을
            포함할 수
            있다`;

let desc2 = '여러줄을 포함하려면 \n 이렇게 사용해야 한다'; // 추가로 한줄로만 가능

// ============length(문자열의 길이)===============

let desc3 = '안녕하세요.';
console.log('=====문자열의 길이====');
console.log(desc3.length); // 6

// ============배열처럼 특정 위치에 접근하기===============
console.log('=====[] 사용====');
console.log(desc2[2]) // 하
// 한글자만 바꾸는 것은 불가능

// ============toUpperCase(),toLowerCase()메서드 사용===============
console.log('======toUpperCase(),toLowerCase()사용=====')
let eng = 'Hi guys. Nice to Meet you.';
console.log(eng.toLowerCase); //소문자
console.log(eng.toUpperCase); // 대문자

// ============str.indexOf(text) 메서드 사용하기.===============
console.log('=====str.indexOf(text)사용====');

console.log(eng.indexOf('to')); // 14 문자열의 시작점을 반환한다
console.log(eng.indexOf('man')); // 만일 찾는 문자가 없다면 -1을 반환한다.
// 찾는 문자가 여러개라도 처음 인덱스만 반환한다

if(eng.indexOf('Hi')){
    console.log('Hi가 포함된 문장입니다.');
} // 위 문장은 실행되지 않는다
// Hi의 시작 인덱스는 0이므로 0은 false이다.
// 그러므로 조건에 부합하지 않는다


if(eng.indexOf('Hi') > -1){
    console.log('Hi가 포함된 문장입니다.');
}//이렇게 하면 실행됨.


// ===========str.slice(n,m)============ 
// n번째부터 m-1 번째까지 반환한다. n이 음수로 시작하면 끝 인덱스부터 시작한다.
console.log('===============str.slice(n,m)==============')
let alpha = 'abcdefg';
console.log(alpha.slice(2)); // 'cdefg'
console.log(alpha.slice(0,5)); // 'abcde'
console.log(alpha.slice(2,-2)); // 'cde'

// ===========str.substring(n,m)============ 
// n과 m사이 문자열을 반환한다 slice와 유사하나 str.substring(m,n) m~n번째 사이 문자열을 반환한다 동작한다!!
// 음수는 0으로 인식
console.log('===========str.substring(n,m)============ ') 

console.log(alpha.substring(2,5)); // 'cde'
console.log(alpha.substring(5,2)); // 'cde'


// ===========str.substr(n,m)============ 
// n부터 시작 m개를 가져옴

console.log('===========str.substr(n,m)============ ')
console.log(alpha.substr(2,4)); // 'cdef'
console.log(alpha.substr(-4,2));// 'de'

// ===========str.trim()============ 
// 앞뒤 공백을 제거한다
console.log('// ===========str.trim()============ ')

let sec = ' coding       ';
console.log(sec.trim()); // coding

// ===========str.repeat(n)============ 
let hello = 'hello!'
console.log('// ===========str.repeat(n)============ ')
console.log(hello.repeat(2)) // hello!hello!

// 문자열도 비교연산자 사용이 가능하다.
// ascii code 기준으로 비교한다.
console.log('// ===========str.codepointAt(0)============ ')

console.log('a'.codePointAt(0));// 97
// 반대로 숫자 코드를 알고있다면 문자열을 얻을 수 있다.
console.log(String.fromCodePoint(97)) // a
console.log('a'<'c');

// includes메소드
// 문자가 있으면 true
// 없다면 false반환.
