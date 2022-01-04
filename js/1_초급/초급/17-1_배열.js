let days = ['월','화','수']
console.log(days[1]); // 화
days[1] = 'tue' // tue로 바꿈

console.log(days.length) // 길이

days.push('목') // 제일 뒤에 추가

days.unshift('일') // 제일 앞

for (let i = 0 ;i <days.length; i++){
    console.log(days[i])
} // 차례로 출력
for (let day of days){
    console.log(day)
}