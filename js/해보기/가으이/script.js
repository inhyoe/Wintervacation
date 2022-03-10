let curPos = 0;       //현재 보여지고있는 이미지번호. 0~3
let positionValue = 0;//이미지 태그의 위치 값 지정할 변수
const IMAGE_WIDTH = 640; // 이만큼 움직인다.

const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");
const images = document.querySelector(".img");

function next(){
    if(curPos<3){
        prevBtn.removeAttribute('disabled')
        positionValue = positionValue-IMAGE_WIDTH;
        images.style.transform = `translateX(${positionValue}px)`
        curPos += 1;
        images.style.transition='0.5s ease-out'
        if(curPos ===3){
            nextBtn.setAttribute('disabled','true')
        }
    }
}


function init(){
    prevBtn.setAttribute('disabled','true')
    nextBtn.addEventListener('click',next)
    prevBtn.addEventListener('click',prev)
};

function prev(){
    if(curPos ===3){
        
        positionValue += IMAGE_WIDTH;
        images.style.transform = `translateX(${positionValue}px)` 
        images.style.transition='0.5s ease-out'
        curPos -= 1;
    }else{
        nextBtn.removeAttribute('disabled')
        positionValue += IMAGE_WIDTH;
        images.style.transform = `translateX(${positionValue}px)`
        images.style.transition='0.5s ease-out'
        curPos -= 1;
        if(curPos ===0){
            prevBtn.setAttribute('disabled','true')
        }
    }
}

prevBtn.addEventListener('click',prev)

init();
