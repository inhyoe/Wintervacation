//배열 재정열
// 배열 자체가 변경
// 무작위 순서를 정렬해줌
var arr = [1,5,4,2,3];
arr.sort()

console.log(arr)

var arr = ['e','a','c','q','r'];
arr.sort();
console.log(arr)

var arr = [27,8,5,13];
// arr.sort();
// console.log(arr) // 1 ,2 ,5 ,8 로 정렬하고 뒤의 숫자는 제외. 정렬하는 요소를 문자열로 받기 때문이다.
// 제대로 하려면? 
// 함수도 인수로 받을 수 있음.
function fn(a,b){
    console.log(a,b);
    return a-b;
}
// 8 ,27을 최초로 받음. => 8,27,5,13
// 5 , 8을 받음  = > 5,8,27,13
// 13, 5 비교 바뀌지 않음
// ...
// 13 27비교했을때 27이 더 크니까 5,8,13,27
console.log(arr);
// 어려우니 lodash참고.
arr.sort(fn);
console.log(arr)

console.log('================reduce()===============')
// 인수로 함수를 빋음
// (누적계산값,현재값) = > {return 계산값}

var arr = [1,2,3,4,5];

var result = 0;
arr.forEach(num =>{
    result += num;
})
console.log(result)//한번에 처리해주는 것이 reduce

var result = arr.reduce((prev, cur)=>{
    return prev + cur;
},0) // prev <- 누적값
     // cur <- 현재값
     // 0 <- 초기값.(생략가능)
     console.log(result)

//ex)
// 성인만 출력하기.
var userList = [
    {name : 'Mike', age:30},
    {name : 'Tom', age:10},
    {name : 'Jane', age:27},
    {name : 'Sue', age:26},
    {name : 'Harry', age:42},
    {name : 'Steve', age:60},

];
var result = userList.reduce((prev,cur)=>{
    if(cur.age > 19){
        prev.push(cur.name);
    }
    return prev;
},[]);

console.log(result)
//나이의 합을 구하기.

var result = userList.reduce((prev,cur)=>{
    return prev = Number(prev)+Number(cur.age)
},0);

console.log(result)
// 이름이 세자.
var result = userList.reduce((prev,cur)=>{
    if((cur.name).length === 3){
        prev.push(cur.name)
    }
    return prev
},[])

console.log(result)