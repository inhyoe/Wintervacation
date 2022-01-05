// function fn(){
//     console.log(3)
// }
// setTimeout(fn,1000)

// function showName(name){
//     console.log(`이름은 ${name}입니다.`)
// }

// setTimeout(showName,2000,'Mike')
var num = 0;
function showName(name) {
    console.log(name)
    console.log(num)
    num++;
    if(num ==5){
        clearTimeout(tId)
    }
}

var tId = setInterval(showName,1200,'Mike')
