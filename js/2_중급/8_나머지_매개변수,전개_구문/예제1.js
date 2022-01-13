function showName(...names){
    console.log(names)
    console.log(names.length)
}

showName('Mike','Tom')

var add = (...num) =>{
    var result = 0;
    result += num;
    return console.log(num)
} // 각각의 원소가 순서대로 들어가는 것이 아니라 한번에 들어감

var add = (...num) =>{
    var result = 0;
    num.forEach(num => {
        result += num
    });
    return console.log(result)
}
add(1,2,3,4,5)

// reduce 함수.

function add(...num){
    var result = num.reduce((prev,cur) => prev+cur) 
    console.log(result)
}
add(1,2,3,4,5,6)

function User(name , age , ...Skill){
    this.name = name;
    this.age = age;
    this.skill = Skill;

}

var user1 = new User('Mike',30,'html','css')
var user2 = new User('Tom',32,'Js','React')

console.log(user1,user2)