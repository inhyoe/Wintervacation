const whiteButton = document.querySelector('#whiteButton')
const blackButton = document.querySelector('#blackButton')
const body = document.querySelector('.body')
const nav = document.querySelector('.nav')
const title = document.querySelector('.title')
function whiteButton1(){
    body.classList.add('white')
    body.classList.remove('black')
    nav.style.borderRight='1px black solid'
    title.style.borderBotton = '1px black solid'
}

function blackButton1(){
    body.classList.remove('white')
    body.classList.add('black')
    nav.style.borderRight='1px white solid'
    title.style.borderBotton = '1px white solid'
}
whiteButton.addEventListener('click',whiteButton1)
blackButton.addEventListener('click',blackButton1)