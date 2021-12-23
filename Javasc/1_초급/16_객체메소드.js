const superman = {
    name : 'Clark', // key
    age : 33 ,      // value
    fly : function(){
        console.log('날아갑니다.'); // fly : (){console.log('날아갑니다')}
    }   
    //key와 value 를 property라고 명명.
}
// 객체 프로퍼티로 할당된 함수를 메서드라고 함.

const user ={
    name : 'Mike',
    sayHello : function(){
        console.log(`Hello, I'm ${this.name}`); // 그냥 nmae이나 user.name은 오류가 발생할 수 있음.
    }                                           // user.satHello 호출시 user == this가됨.
}
// 예제

let boy = {
    name : 'Mike',
    sayHello : function(){
        console.log(`Hello, I'm ${this.name}`);
    }
}

let girl = {
    name : 'Jane',
    sayHello : function(){
        console.log(`Hello, I'm ${this.name}`);
    }
} // 이렇게 호출시 화살표 함수로 호출히면 전혀 다른 값을 가져옴
  // 화살표 함수는 함수와는 달리 this를 가지지 않으며 this사용시 외부에서 값을 가져옴.

  let boy = {
    name : 'Mike',
    sayHello : ()=>{
        console.log(`Hello, I'm ${this.name}`);
    } // this != boy 전역 객체를 가져옴
}     // 브라우저 : window <-- 어렵다.


