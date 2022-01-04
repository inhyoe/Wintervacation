var superman = {
    name : 'Clark', // key
    age : 33        // value
    //key와 value 를 property라고 명명.
}
// 접근방법
superman.name //clark
superman.age // 33

// 추가
superman.gender = 'male';
superman['haircolor'] = 'black';

// 삭제

delete superman.name;

// 단축 프로퍼티

var name = 'clark';
var age = 33;

var superman = {
    name : name, // 축약 name
    age : age, //   축약   age
    gender : 'male'
}
//프로퍼티 존재 여부 확인
var superman = {
    name : name, // 축약 name
    age : age, //   축약   age
    gender : 'male'
} //일 때

superman.birthday; // undefined 출력
// ==
'birthday' in superman; // false 출력
'age' in superman //true 출력

// for in 반복문 사용 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for(let key in superman){
    console.log(key)
    console.log(superman[key])
}
// 예제
var superman = {
    name : 'Clark', // key
    age : 33        // value
    //key와 value 를 property라고 명명.
}
superman.haircolor = 'Black';
superman['hobby'] = 'football';
delete superman.age;
console.log(superman)

// 예제 2
function makeObject(name,age){
	return{
		name : name, // name
		age : age,   // age 으로 축약 가능 
		hobby : 'football'
	};
} // 함수 생성 후

var Mike = makeObject('Mike',22); // 값을 넣어줌
console.log(Mike); // 호출
// 예제2를 화살표 축약으로 만들자

var makeObject = (name,age) =>{
	return{
		name : name, // name
		age : age,   // age 으로 축약 가능 
		hobby : 'football'
	};
} // 함수 생성 후


var Mike = makeObject('Mike',22);
console.log(Mike)

console.log(Mike.age) //22
console.log('age' in Mike)// true
console.log(Mike.birthday) // undefined
console.log('birthday' in Mike) // false


function isAdult(user){
    if(user.age < 20){
        return false;
    }else{
		return true;
}
}

var Mike ={
    name : 'Mike',
    age : 30
};
var Jane ={
    name : 'Jane'
};

console.log(isAdult(Mike));
console.log(isAdult(Jane)); // undefined 라서 if 문에서 true를 반환

// 수정
function isAdult(user){
    if(user.age < 20 || !('age' in user)){ // 느낌표를 붙인다  user에 age가 없으면 true 있으면 false
        return false;
    }else{
		return true;
}
}

var Mike ={
    name : 'Mike',
    age : 30
};
var Jane ={
    name : 'Jane'
};

console.log(isAdult(Mike));
console.log(isAdult(Jane)); // undefined 라서 if 문에서 true를 반환
