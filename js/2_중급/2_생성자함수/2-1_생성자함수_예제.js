// 생성자 함수 : 상품 객체를 만들어보자

function Item(title,price){
    //this = {}
    this.title = title;
    this.price = price;
    this.showprice = function(){
        console.log(` ${title}의 가격은 ${price}원 입니다.`);
    }
    //return this;
}

const item1 = new Item('인형',3000);
const item2 = new Item('가방',4000);
//const item2 = Item('가방',4000); new를 붙이지 않으면 undefined가 실행이됨. == 함수가 실행이 된다. return값이 없기때문이다.
const item3 = new Item('지갑',9000);
console.log(item1,item2,item3);  // Item{title : '인형', price: 3000, showPrice : f}
                                 //  Item{title : '인형', price: 3000, showPrice : f}
                                 //  Item{title : '인형', price: 3000, showPrice : f} 출력

item3.showprice(); // 가격은 9000원입니다.