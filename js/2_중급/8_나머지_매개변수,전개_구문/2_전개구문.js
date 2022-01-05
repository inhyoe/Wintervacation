var arr1 = [1,2,3]
var arr2 = [4,5,6]

var result = [...arr1,...arr2]
console.log(result)
var result = [0,...arr1,...arr2,7,8,9];
console.log(result)

arr1.push(arr2) //  [ 1, 2, 3, [ 4, 5, 6 ] ]
var arr1 = [1,2,3]
var arr2 = [4,5,6]
arr3 = []
arr3 = arr1+arr2
console.log(arr3) // 1,2,34,5,6

var arr = [1,2,3];
var arr2 = [...arr];

var user = {name:'Mike',age:30}; //Object자료형
var user2 = {...user}
user2.name = 'Tom';
console.log(user.name)
console.log(user2.name) // ObjectAssgin을 사용할 필요가 없다.

// arr1을 [4,5,6,1,2,3]으로 만들기

var arr1 = [1,2,3];
var arr2 = [4,5,6];
// 일반적인 방법
arr2.forEach(num => {
    arr1.unshift(num) // 숫자가 하나씩 밀림.
})
console.log(arr1)

var arr1 = [1,2,3];
var arr2 = [4,5,6];
arr2.reverse().forEach(num => {
    arr1.unshift(num) // reverse로 역순으로 넣어줌.
})
console.log(arr1)

var arr1 = [1,2,3];
var arr2 = [4,5,6];
var arr1 = [...arr2,...arr1]
console.log(arr1)

var user = {name : 'Mike'}
var info = {age : 30};
var fe = ['JS','React']
var lang = ['Korean','English']
user = Object.assign({},
    user,
    info,
    {Skills : []}, {lang : []})

    fe.forEach(num => {
        user.Skills.push(num)
    })
    lang.forEach(num => {
        user.lang.push(num)
    })
    console.log(user)

var user = {name : 'Mike'}
var info = {age : 30};
var fe = ['JS','React']
var lang = ['Korean','English']

var user = {
    ...user,
    ...info,
    Skills : [...fe,...lang]
}
console.log(user)
