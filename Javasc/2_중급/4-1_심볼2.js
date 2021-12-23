// 다른 개발자가 만들어놓은 객체

const user = {
    name : "Mike",
    age : 30
};

// 내가 작업



// user.showName = function(){}; // showName이 키이고 fucntion(){} 이 값이 됨.

 const showName = Symbol('show name'); // 심볼 생성
user[showName] = function(){
 console.log(this.name);
}; // 심볼인 showName을 사용했으므로 나타나지않음


user[showName](); // 호출하는 방법.

// 사용자가 접속하면 보는 메세지

for (let key in user){
    console.log(`His ${key} is ${user[key]}.`)
}