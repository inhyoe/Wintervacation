const obj = {
    1 : '1입니다',
    false : '거짓'
}

Object.keys(obj); // ['1','false']
console.log(obj['1']) // 1입니다
console.log(obj['false']) // 거짓  문자열로도 접근 가능.

// Symbol형

const a = Symbol();
const b = Symbol();
console.log(a);
console.log(b);
console.log(a==b) // 자료형은 달라도 내용이 다르면 false
console.log(a===b) // 일치연산자 false

const id = Symbol('id');
const id2 = Symbol('id2');
console.log(id)
console.log(id2)

const id3 = Symbol('id3');
const user1 = {
    name : 'Mike',
    age : '30',
    [id3] : 'myid' // computed property key
};
console.log(user1)
console.log(user1[id3])
console.log(Object.keys(user1)) // id3를 건너뜀.
Object.values(user1)
console.log(Object.entries(user1)) // 키가 심볼형이면 건너뜀.
for( let a in user1){} // 또한 건너뜀

// 그럼 어디서 쓰나?

const user2 = {
    name : 'Mike',
    age : 30
} // 일 때

const id7 = Symbol('id');
user2[id7] = 'myid' // 추가할때 사용법 ,
// 장점 : 객체에 내용을 추가할때 원본을 추가할때 용이함.

//================================================
// Symbol.for() : 전역심볼
// 하나의 심볼만 보장받을 수 있음
// 없으면 만들고, 있으면 가져오기때문
// Symbol 함수는 매번 다름 symbol값을 생성하지만
// Symbol.for 메소드는 하나르 생성한 뒤 키를 통해 같은 Symbol을 공유한다

const id4 = Symbol.for('id4');
const id5 = Symbol.for('id5');
console.log('===========Symbol.for메서드 ===========');
console.log(id4 === id5) // for 을 사용하지 않을때에 비해 값이 다른 true가 생성된다.
console.log('===========keyFor메소드===========');
console.log(Symbol.keyFor(id4)) // 생성할때 만든 값을 알려줌
// 전역심볼이 아닌 값은 ketFor 사용 불가능. 대신 
console.log('===========dsecroption메소드 ===========');
console.log(id.description) // 사용가능
// 다만 심볼로 완벽히 숨길 수는 없다.
console.log('===========getOdwnPropertSymbols ===========')
console.log(Object.getOwnPropertySymbols(user2)) // 심볼만 출력 가능.

