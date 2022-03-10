console.log('안녕하세요');

console.log('number. %d ', 10);

console.log('String %s','hi');

var person ={
    name : '소녀시대'
    ,age : 20
}

console.log('js 객체 .%j',person);

console.dir(person);
//객체 그대로를 보여줌

console.time('duration_time');

var result = 0;
for ( var i =0; i<10000;i++){
    result +=1;
}
console.timeEnd('duration_time')

console.log('파일 이름 : %s',__filename);
//실행되는 파일 이름
console.log('패스 : %s' , __dirname);
//실행되는 파일의 경로