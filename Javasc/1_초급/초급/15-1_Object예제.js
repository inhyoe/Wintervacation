// 예제
const superman = {
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

const Mike = makeObject('Mike',22); // 값을 넣어줌
console.log(Mike); // 호출
// 예제2를 화살표 축약으로 만들자

const makeObject = (name,age) =>{
	return{
		name : name, // name
		age : age,   // age 으로 축약 가능 
		hobby : 'football'
	};
} // 함수 생성 후


const Mike = makeObject('Mike',22);
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

const Mike ={
    name : 'Mike',
    age : 30
};
const Jane ={
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

const Mike ={
    name : 'Mike',
    age : 30
};
const Jane ={
    name : 'Jane'
};

console.log(isAdult(Mike));
console.log(isAdult(Jane)); // undefined 라서 if 문에서 true를 반환


//3

const Mike = {
    name : "Mike",
    age : 30};

for (x in Mike){
    console.log(x)
} // key값들 대입

for (x in Mike){
    console.log(Mike[x])
} // key을 value 대입
