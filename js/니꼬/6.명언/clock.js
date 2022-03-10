const clock = document.querySelector("h2#clock")
        function getClock(){
            let hours = new Date().getHours();
            let Minutes = new Date().getMinutes();
            let Seconds = new Date().getSeconds();
            let realHours = String(hours).padStart(2,"0");
            let realMinutes = String(Minutes).padStart(2,"0");
            let realSecond = String(Seconds).padStart(2,"0");
            // new Date(). ... 는 숫자이기때문에
            // padStart는 적용되지 않으므로 String형으로 바꾸ㅓ줘야 함.
            // padStart("문자열의 길이","앞의 대체할 문자열")
            
            clock.innerText = `${realHours}:${realMinutes}:${realSecond}`
        }
        
        setInterval(getClock,1000)