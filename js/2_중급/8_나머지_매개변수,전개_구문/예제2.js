var arr1 = [1,2,3]
var arr2 = [4,5,6]

var result = [...arr1,...arr2]
console.log(result)

arr1.reverse().forEach( num => {
    arr2.unshift(num)
})
console.log(arr2)

arr1.forEach(num =>{
    arr2.shift(num)
    console.log(arr2)
})

console.log(arr2) // ====>

arr1.reverse()
console.log(arr1)
arr2 = [...arr1,...arr2]
console.log(arr2)

var result = arr2.reduce((end,str) =>{
    end += str;
    return end
})

console.log(result)

// user 객체에 넣어보자.
var user = {name : 'Mike'}
var info = {age : 30};
var fe = ['JS','React']
var lang = ['Korean','English']

user = Object.assign({},
    user,
    info,
    {Fe : []},{lang : []})
    
fe.forEach(num => {
    user.Fe.push(num)
})
lang.forEach(num => {
    user.lang.push(num)
})

console.log(user)
var user = {name : 'Mike'}
var users = {
    ...user,...info, Skill : [...fe,...lang]
}

console.log(users)