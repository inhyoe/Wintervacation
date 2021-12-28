let boy = {
    name : 'Mike',
    showname : function(){
        console.log(boy.name);
    }
};

boy.showname()

let man = boy;
man.name = 'Tom';

console.log(boy.name) // boy의 name도 Tom으로 바뀌었다.
boy = null;
man.showname() // Error 출력 , 왜냐하면 boy.name이기때문이다. 개선하기 위해선 객체를 가리키는 this를 사용한다.

// 화살표 함수 사용
let boy = {
    name : 'Mike',
    showname : () => {
        console.log(this.name);
    }
};

boy.showname() // 해당 객체의 브라우저 페이지가 나타나고 this사용시 window가 출력되므로
               // 화살표 함수 사용시에는 this를 사용하지 않는것이 좋다.