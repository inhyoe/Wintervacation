// push() 뒤에 삽입
// pop()  뒤에 삭제
// unshift() 앞에 삽입
// shift()  앞에 삭제
//======================= arr.splice(n,m,x) : 특정 요소를 지움 =======================
// n부터 시작해서 m개를 지움 특정 요소를 지우고 x만큼 추가.
console.log('======================= arr.splice(n,m) : 특정 요소를 지움 =======================')
let arr = [ 1,2,3,4,5];
arr.splice(1,2); // 1부터시작해서(1포함하여) 2개의 원소를 삭제함
console.log(arr); // 1,4,5

let arr2 = [1,2,3,4,5];
arr2.splice(1,3,100,200,300);
console.log(arr2); // 1,100,200,300,5

let arr3 = ['나는','철수','입니다']
arr3.splice(2,0,'대한민국',1,'번째','소방관') // m값에 0이 추가된 경우 아무것도 지우지않고 n번째 원소 이전부터 추가함.
console.log(arr3)

//======================= arr.splice() : 삭제된 요소를 반환한다. =======================

console.log('======================= arr.splice() : 삭제된 요소를 반환한다. =======================')
let arr4 = [1,2,3,4,5];
let result = arr4.splice(1,2); // 삭제된 요소를 반환한 값을 result에 넣었음.
console.log(result); // 2,3
console.log(arr4)

//======================= arr.slice(n,m) : n부터 m-1까지 반환한다. =======================
console.log('======================= arr.slice(n,m) : n부터 m-1까지 반환한다. =======================')
let arr5 = [1,2,3,4,5];
console.log(arr5.slice(1,4)); // 1~3번째 인덱스까지 반환한다.
console.log(arr5.slice()) // 기존 배열을 반환한다.

//======================= arr.concat(arr2,arr3 ..) : 배열을 합쳐서 반환한다. =======================
console.log('===========arr.concat(arr2,arr3 ..) : 배열을 합쳐서 반환한다.=============')

let arr6 = [1,2,3];
let arr7 = [4,5,6,7];
let arr8 = [8,9,10,11,12];

console.log(arr6.concat(arr7,arr8)) // 하나의 배열임.

//================ arr.forEach(fn) : 배열 반복. ===========================
console.log('================ arr.forEach(fn) : 배열 반복. ===========================');

let user = ['Mike', 'Tom','Jane'];
user.forEach((item,index, arr) => {});
// forEach는 함수를 인덱스로받는다
// item 은 'Mike'Tom,Jane이고
// index 는 말 그래도 0 , 1 ,2 이고
// arr 은 해당 배열 그자체를 의미한다.
user.forEach((name,index)=>{
    console.log(`${index+1}. ${name}`);
})
// 배열을 순서대로 반복한다.

// ============== arr.indexOf / arr.lastIndexOf =============
console.log('============== arr.indexOf / arrlastindexOf =============')
// arr.indexOf는 처음부터 찾는것
// arr.lasindexOf는 끝부터 찾는것
let arr9 = [1,2,3,4,5,6,1,3];
console.log(arr9.indexOf(3)) // 3이 있는 제일 처음 위치를 출력
console.log(arr9.indexOf(3,3)) // 인덱스번호 3번째부터 3을 출력한다.
console.log(arr9.lastIndexOf(3)) // 끝에서부터 탐색하여 인덱스 번호를 출력한다.
console.log(arr9.lastIndexOf(6,6)) // 처음 n은 원소를 가르키는 것으고 마지막 m은 인덱스 번호부터 지정을 하는 것 이다.


// ============== arr.includes() : 포함하는지 확인 =============

console.log('arr.includes() : 포함하는지 확인')
let arr10 = [1,2,3];
console.log(arr10.includes(2)) // true
console.log(arr10.includes(8)) // false

// ============== find/findIndex : indexOf와 동일하지만 함수를 연결할 수 있다.  =============
console.log('=============find/findIndex : indexOf와 동일하지만 함수를 연결할 수 있다.================');
// 첫번째 true값만 반환하고 끝,
// 만일 없다면 undefined를 반환한다.
// findIndex는 인덱스 번호를 반환한다.
let arrr = [1,2,3,4,5];

const result1 = arrr.find((item) => {return item%2 == 0;
});
console.log(result1); // 4도 포함이 되지만 4는 출력이 되지 않는 모습.

let userList = [
    {name : 'Mike', age : 30},
    {name : 'Jake', age : 27},
    {name : "Tom", age : 10}
];

const result2 = userList.findIndex((user)=> {
    if(user.age < 19){
        return true;
    }else{
        return false;
    }
})
console.log(result2) 

// 조건을 할고싶은 모든 요소를 배열로 반환하는 메서드
// ================= arr.filter(fn) ==================== 
console.log('================= arr.filter(fn) ==================== ')

const result3 = arrr.filter((item) => {return item%2 == 0;
});
console.log(result3); // find 함수와 다르게 조건에 맞는 원소를 배열로 표현 .

// ================= arr.reverse ====================
// 역순으로 재정렬한다.
console.log('================= arr.reverse ====================')
let array = [1,2,3,4,5];
console.log(array.reverse())

// ================= arr.map(fn) ====================
// 함수를 받아 특정 기능을 시행하고 새로운 배열을 반환
console.log('================= arr.map(fn) ====================')

let userList1 = [
    {name : 'Mike' , age: 30},
    {name : 'Jane' , age: 27},
    {name : 'Tom' , age: 10},
]; // 배열에 객체를 넣은 것이다.

let newUserList = userList1.map((user, index) => {
    return  Object.assign({}, user,{
        id : index + 1,
        isAdult : user.age >19    }); // assgin 메서드의 초기값은 처음 값, 두번째느 배열 세번째는 조건식과 들어가는 값들.
});
console.log(newUserList);