function User(name,age){
    this.name = name;
    this.age = age;
} // 붕어빵틀 관례로 첫글자는 대문자

let User1 = new User('Mike',30); // 붕어빵
let User2 = new User('Jane',22);
let User3 = new User('Tom',18);

// 만일 new User(); 을 실행하면
// 생성자 User 내에서 this = {}라는 빈 객체를 생성하고 this에 할당함
// this에 프로퍼티 ( name , age ) 를 추가함.
// return this를 반환함.
function User(name,age){
    // this = {};
    this.name = name;
    this.age = age;
    // return this;
} // 붕어빵틀

// -------------------------
function User(name,age){
    this.name = name;
    this.age = age;
    this.sayname = function(){
        console.log(this.name);
    }
} // 붕어빵틀
let User5 = new User('Tommy',23);
console.log(User5)
User5.sayname(); // Tommy
//this는 생성자의 이름.
