alert // 알려줌
prompt // 입력받음
confirm // 확인받음

const name = prompt('이름을 입력하세요.'); // 파이썬의 input
alter('환영합니다, ' + name + '님') // 화면에 출력해줌.
alter(`환영합니다, ${name}님. 환영합니다.`); // 위와 같음 (벡틱이라 표시)
//만일 취소시 null이 출력. == 값이 없다.
//프롬프트는 두개의 인수를 받을수있다 첫번째 값은 화면 출력시 나오는 값이고 두번째값은 출력문에 나오는 값이다.
//ex)
const name = prompt('예약일을 입력하세요.', '2021-10-')

// confirm 확인받을때

const isAdult = confirm("당신은 성인입니까?"); // 확인과 취소버튼이 같이 있음
console.log(isAdult) // 확인은 true 취소는 false

//단점 창이 떠있는동안 스크립트 일시 정지
//스타일링을 할 수 없다.

//장점 빠르고 간단하게 적용 가능함.