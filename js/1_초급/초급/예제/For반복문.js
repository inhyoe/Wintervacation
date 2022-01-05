// 일반적인 반복문

for (var i =0 ; i < 5; i++ ){
    var result = 0;
    result += i;
}
console.log(result)


// for in 반복문 (객체에 사용가능)
user = { name : 'Tom',
         age  : 30,
         Skill : 'JS'}

for( var key in user){
    console.log(key,user[key])
}

// forEach반복문 오직 Array에만 사용 가능하다.

user = [ 1,2,3,4,5,6]

user.forEach(element => {
    if(element%2 == 0 ){
        console.log(element,'는 짝수')
    }else{
        console.log(element,'는 홀수')
    }
});

