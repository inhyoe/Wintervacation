// return을 사용

function add(num1, num2){
    return num1 + num2;
}

const result = add(num1,num2);
console.log(result)

// return문이 없을때?

function showError(){
    alert('에러가 발생하였습니다')
    return; // return문 이후의 내용은 실행되지 않음.
    alert('이 코드는 절대 실행되지 않음.')
}
const result = showError()
console.log(result) // alert문 반환 후 ,undefined 반환
