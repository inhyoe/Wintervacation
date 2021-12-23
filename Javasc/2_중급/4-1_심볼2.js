// 다른 개발자가 만들어놓은 객체

const user = {
    name : "Mike",
    age : 30
};

// 사용자가 접속하면 보는 메세지

for (let key in user){
    console.log(`His ${key} is ${user[key]}.`)
}