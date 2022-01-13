setTimeout // 일정 시간이 지난 후 함수를 실행
setInterval //일정 시간 간격을 함수를 반복

function fn(){
    console.log(3)
}
setTimeout(fn,3000) // 3초 뒤에 fn을 반환함.
// ==
setTimeout(function fn(){
    console.log(3)
},3000) // 동일

function showName(name){
    console.log(name)
}

setTimeout(showName,3000,'Mike') // Mike라는 인자를 name에 전달받음.
//          함수     시간   인자값

//clearTimeout() 예정된 작업을 없엔다.

var tId = function showName(name){
    console.log(name)
}

setTimeout(showName,3000,'Mike')


// setInterval은 setTimeout과는 다르게 계속 반복한다
// 종료하려면 clearInterval을 사용한다.

var tId = function showName(name){
    console.log(name)
}

setTimeout(showName,3000,'Mike') // Mike ......
clearInterval(tId) // 종료.

// 만약 딜레이가 0이라면?

setTimeout(function(){
    console.log(2)
},0)           // 후에 실행.
console.log(1) // 먼저 실행후
