// call aply bind : 함수 호출 방식과 관계없이 this를 지정할 수 있음.

// call 모든 함수에서 사용 할 수있으며 this를 특정값으로 지정할 수 있다.

var mike = {
    name : 'Mike'
};

var tomd = {
    name : 'Tom'
}

function showName(){
    console.log(this.name)
}

showName() // 아무것도 가리키지 않았기 때문에 window가 호출이 된다

showName.call(mike) // this로 사용할 객체를 대입.

function update(birthYear,occupation){
    this.birthYear = birthYear;
    this.occupation = occupation
}

update.call(mike,1990,'singer')
console.log(mike)
// 첫번째는 사용할 객체이고 두번째부터 매개변수이다.
update.call(tomd,1990,'singer')
console.log(tomd)

//apply는 함수에 사용하며 **매개변수를 배열**로 받는다

update.apply(mike,[1990,'singer'])
update.apply(tomd,[1992,'teacher'])

console.log(mike)
console.log(tomd)

var nums = [ 3, 10 ,1 , 6, 4]

var minNum = Math.min(...nums);
var maxNum = Math.max(...nums); // 배열이기때문에 err 그러므로

var minNum = Math.min(...nums)
var maxNum = Math.max(...nums); // 
console.log(maxNum)
console.log(minNum)

// apply

var minNum = Math.min.apply(null,nums) // 배열을 받기 때문이다.
// ==>
var minNum = Math.min.call(null,...nums) // 배열을 받지 않는다

var maxNum = Math.max.apply(null,nums) // 배열을 받기 때문
var maxNum = Math.max.call(null,...nums) // 배열 x

console.log(minNum)
console.log(maxNum)

//bind this값을 영구히 바꿀 수 있다

var mike = {
    name : 'Mike'
}
function update(birthYear,occupation){
    this.birthYear = birthYear;
    this.occupation = occupation
}

var updateMike = update.bind(mike);

updateMike(1980,'police') 
console.log(mike)

var user ={
    name : 'Mike',
    showName : function(){
        console.log(`hello, ${this.name}`)
    }
}

var fn = user.showName;

fn.call(user)
fn.apply(user)

var boundfn = fn.bind(user);
boundfn()