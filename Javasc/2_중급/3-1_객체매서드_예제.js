// let n  = 'name';
// let a = 'age';

// const user = {
//     [n] : 'Mike', // name
//     [a] : 30 ,     // age
//     [1+2] : 3
// };

// console.log(user);

function makeObj(key,val){
    return{
        [key] : val
    }
};
const obj = makeObj('나이',33);

console.log(obj);

// 객체 메서드

const user = {
    name : 'Mike',
    age : 30
};

// const user2 =  user ;// x
// user2.name = "Tom";
// console.log(user);
// console.log(user2); // 두개의 이름이 바뀜.

//개선하기 위해선

const user2 = Object.assign({},user); // 초기값에  {} 빈객체에 , user를 넣는다 .
user2.name = 'Tom';
console.log(user);
console.log(user2)

