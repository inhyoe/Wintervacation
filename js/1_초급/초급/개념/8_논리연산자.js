const name = prompt('남자입니까?');
const age = Number(prompt('나이를 입력하세여'));

if (name == '남자' && age >20){
	console.log('입대하셔야합니다.')
}else if( name == '남자' && age <20 ){
	console.log('입대하지 않으셔도 됩니다')
}else{
	console.log( '여자는 입대하지 않으셔도 됩니다' )
}

// && == and
// || == or
// 비교 연산자도 우선순위가 있다 , and 가 or 보다 우선순위

const gender = 'F';
const name = 'Jane';
const isAdult = true;
// if(gender == "M" , && name == 'Mike' || isAdult){ 이 코드는
//if((gender == "M" && name == 'Mike') || isAdult){ // 이 코드와 같다.
if(gender == "M" && (name == 'Mike' || isAdult)){ // 이것이 의도된 바.

    console.log('통과')
}else{
    console.log('통과')
}