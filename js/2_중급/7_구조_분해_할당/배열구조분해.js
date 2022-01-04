var [x,y] = [1,2];

console.log(x)
console.log(y)

var users = ['Mike','Tom','Jane'];

var [user1,user2,user3] = users;

console.log(user1) // users[0]
console.log(user2) // users[1]
console.log(user3) // users[2]

var str = 'Mike-Tom-Jane';

var [user1,user2,user3] = str.split('-')
console.log(user1) // str.split('-')[0]
console.log(user2) // users[1]
console.log(user3) // users[2]

var [a,b,c] = [1,2];
console.log(a);
console.log(b);
console.log(c) // undefined 
// 이러한 에러를 발생시키지 않기 위해 기본값을 할당한다
console.log('============기본값할당==========')
var [a=1,b=2,c=3] =[3,4]
console.log(a) 
console.log(b)
console.log(c) // 기본값 할당

//일부 반환값 무시

var [user1, ,user2] = ['Mike','Tom','Jane','Tony'];
console.log(user1) //Mike
console.log(user2) //Jane

// 배열 구조 분해 바꿔치기
// 일반적으론 임시변수를 하나 이상 만들고 사용해야함

var a = 1;
var b = 2;
var c = a;
var a=b;
var b=c;
console.log(a,b,c)// 번거롭다
// 배열 구조 분해에서는
console.log('===========배열 구조 분해 바꿔치기 =========')
var [a,b] = [1,2];
console.log(a,b)
var [a,b] = [b,a];
console.log(a,b) // 임시변수 c는 필요없어짐


//객체에서도 사용 가능하다
var user = {name: 'Mike',age : 30};
var {name,age} = user;
// == var name = user.name 
// == var age = user.age
// 순서를 바꿔서 사용해도 사용 가능하다.
var user = {name: 'Mike',age : 30};
var {age,name} = user;
console.log(name);
console.log(age)

// 새로운 변수 이름으로 할당 가능하다.
var { name : userName,age:userAge} = user;
console.log(userName);
console.log(userAge)

var user ={
    name : 'Mike',
    age : 30,
    
}
var {name ,age,gender} = user // gender는 undefined이다.
var {name ,age,gender = 'male'} = user // 기본값을 할당 가능하다. 단,
var user ={
    name : 'Mike',
    age : 30,
    gender : 'Female'   
}
var {name ,age,gender = 'male'} = user // 이와같이 되었을때
console.log(gender) // male 으로 기본값을 설정했지만 gender 는 Female로 바뀌지 않음
