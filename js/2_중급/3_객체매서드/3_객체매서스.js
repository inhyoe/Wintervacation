let a = 'age'; // 이 age가 user객체에 a에 대입된다.

const user = {
    name : 'Mike',
    [a] : 30 // 변수 a에 할당된 값  컴퓨티트 프로퍼티
} // Object 객체 생성.

const user = {
    [ 1 + 4 ] : 5,
    ["안녕" + "하세요"] : 'Hello'
}

console.log(user) // 5:5, 안녕하세요 : hello

//객체메서드
let a = 'age';
const user = {
    name : 'Mike',
    [a] : 30 // 변수 a에 할당된 값  컴퓨티트 프로퍼티
} // Object 객체 생성.

const cloneUser = user; // 이것은 객체에 대한 값이 저장된 것이 아닌 메모리 참조값이 저장되므로 의도된 바가 아님.
// 복사하려면

const cloneUser = Object.assign({},user); // 빈 객체는 초기값 , 두번째부터 대입되는 값들
// {} + { name : 'Mike', age : 30} =

// ex

const a = Object.assign({gender : 'male'}, user);
console.log(a) // gender : 'male'
               // name : 'Mike'
               // age : 30
// 만일 키값이 같다면?

Object.assign({name : 'Jane',user}) // 덮어쓰게됨.

// 만일 값이 2개 이상이라면
const user = {
    name : 'Mike',
}
const info1 = {
    age : 30
}
const info2 = {
    gender : 'Male'
}
Object.assign(user,info1,info2); // user로 옮겨감.
// ----------------------------

//Object.keys() : 키를 배열로 반환한다

const user = {
    name : 'Mike',
    age : 30,
    gender : 'Male'
}
console.log(Object.keys(user));

//Object.values() : 키값을 배열로 반환

console.log(Object.values(user));

// Object.entries() : 키/값 배열 반환

Object.entries(user);

// Object.fromEntries() : 키/값 배열을 *객체* 로 반환

const arr = Object.entries(user);
Object.fromEntries(arr);