let curPos = 0;       //현재 보여지고있는 이미지번호. 0~3
let positionValue = 0;//이미지 태그의 위치 값 지정할 변수
const IMAGE_WIDTH = 640; // 이만큼 움직인다.

const prevBtn = document.querySelector(".prev");
const nextBtn = document.querySelector(".next");
const images = document.querySelector(".img");
makeClone()

function makeClone(){
    let slide_first = images.firstElementChild.cloneNode(true);
    let slide_last = images.lastElementChild.cloneNode(true);
    // images.insertBefore(slide_last,images.firstElementChild);
    images.append(slide_first);
}
function next(){
    if(curPos<4){
        prevBtn.removeAttribute('disabled')
        positionValue = positionValue-IMAGE_WIDTH;
        images.style.transform = `translateX(${positionValue}px)`
        console.log(positionValue)
        curPos += 1;
        images.style.transition='0.5s ease-out'
        console.log(curPos)
        var change = setTimeout(() => {
            if(curPos ==4){
                positionValue =0;
                console.log(positionValue)
                images.style.transform = `translateX(${positionValue}px)`
                images.style.transition='0s ease-out'
                curPos = 0;
                
            }
            clearTimeout(change)
        }, 500);
    }
    
    
}

var move = null;
function lastNext(){
    
//     if(curPos ==4){
//         positionValue =0;
//         console.log(positionValue)
//         images.style.transform = `translateX(${positionValue}px)`
//         images.style.transition='0s ease-out'
//         curPos = 0;
//     }


// }
}



function init(){
    prevBtn.setAttribute('disabled','true')
    nextBtn.addEventListener('click',next)
    prevBtn.addEventListener('click',prev)
    // nextBtn.addEventListener('click',lastNext)
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

init()