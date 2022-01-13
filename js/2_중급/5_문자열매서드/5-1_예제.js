let list = [
    '01. 들어가며',
    '02. 자료형의 역사',
    '03. 자료형',
    '04. 함수',
    '05. 배열'
];
// for문을 이용하자
let newlist = [];
for(let i=0; i<list.length;i++){
    newlist.push( // 초급 17장 배열에 나옴.
        list[i].slice(4)
    );
};
console.log(newlist)


// 금칙어 : 콜리
// indexOf 메소드 사용.
function hasCola(str){
    if(str.indexOf('콜라') > -1){
        console.log('금칙어가 있습니다')
    }else{
        console.log('통과')
    }
}

hasCola('와 사이다가 짱이야'); 
hasCola('와 콜라가 짱이야');
hasCola('와 맥주가 짱이야');

//includes 를 사용해보자
function hasCola(str){
    if(str.includes('콜라')){
        console.log('금칙어가 있습니다')
    }else{
        console.log('통과')
    }
}

hasCola('와 사이다가 짱이야'); 
hasCola('와 콜라가 짱이야');
hasCola('와 맥주가 짱이야');