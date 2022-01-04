var array = [  {name : 'Mike' , age: 30},
                {name : 'Jane' , age: 27},
                {name : 'Tom' , age: 10},
]

let newList = array.map(function(user,index){
    return Object.assign({} , user,{
        isAdult :user.age > 19
    });
})
// 배열에 접근 한 후 Object객체에 assgin 메소드를 사용함.(객체의 복사)

console.log(newList)
console.log(array[1].name); // 배열의 객체값에 접근하는 방법.
console.log(array.keys())

console.log(Object.assign({},array))


// var numbers = [4,9,16,25,36];
// var result =  numbers.map(Math.sqrt);
// console.log(result)

// var numbers = [1,2,3,4,5,6,7,8,9];
// var newNumbers = numbers.map(numbers => numbers * 2);
// var newNumbers = numbers.map(function number(){numbers *2});

// console.log(newNumbers)
// var numbers = [1,2,3,4,5,6,7,8,9];
// var newNumbers = numbers.map(function(number){ 
//     return number *2}); // return을 꼭 작성해 주자.
// console.log(newNumbers)

var student = [
    {id :1 , name : 'Jonn'}, 
    {id :2 , name : 'Jane'},
    {id :3 , name : 'Tim'},
    {id :4 , name : 'Brian'}

]
var names = student.map(student => student.name)
var names = student.map(function(students){
    return students.name;
})
var id = student.map(students => students.id)
console.log(names)
console.log(id)

var numbers = [[1,2,3],[4,5,6],[7,8,9]];
var newNumbers= numbers.map(array => array.map(number => number *2));
console.log(newNumbers)
// 맵을 한번만 해주면 한개씩 빼는것이므로 배열을2를 곱할 수는 없다.
