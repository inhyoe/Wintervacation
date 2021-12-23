// const user = {
//     name : 'Mike',
//     age : 30,
//     gender : 'Male'
// }
// console.log(Object.keys(user));

const user = {
    name : 'Mike',
}
const info1 = {
    age : 30
}
const info2 = {
    gender : 'Male'
}
Object.assign(user,info1,info2);
console.log(user); // 객체
console.log(Object.values(user)); //values
console.log(Object.entries(user)); // entries
const arr = Object.entries(user);
console.log(Object.fromEntries(arr)); //fromEntries