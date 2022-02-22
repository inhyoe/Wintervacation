const loginInput = document.querySelector('#login-form input')
		const loginForm = document.querySelector('#login-form')
		const greeting = document.querySelector('#greeting')
		const HIIDEN_CLASSNAME = 'hidden'
        const USERNAME = 'username'
        
		function onLoginSubmit(tomato){
            const username = loginInput.value    
			event.preventDefault(); // 브라우저의 기본 동작을 막는다
			loginForm.classList.add(HIIDEN_CLASSNAME); // classname을 추가하기.
			localStorage.setItem(USERNAME,username);  // localStorage에 유저의 이름을 추가하기
            paintGreeting(username) // 
		}
		
		loginForm.addEventListener('submit',onLoginSubmit)

        const saveUserName= localStorage.getItem(USERNAME); // localStorage는 작은 DB
        console.log(saveUserName);
        
        function paintGreeting(username){
            greeting.classList.remove(HIIDEN_CLASSNAME); // 클래스이름인 hidden을 없애기
            greeting.innerText =`Hello ${username}`; // id 이름이 greeting인 것에 텍스트를 추가하기.
        }

        if (saveUserName === null){
            loginForm.classList.remove(HIIDEN_CLASSNAME); 
            loginForm.addEventListener('submit',onLoginSubmit);
        }else{
            paintGreeting(saveUserName);
        }