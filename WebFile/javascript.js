const toggleBtn = document.querySelector('.navbar_tooglebutton');
const menu = document.querySelector('.navbar_menu') 
const navbar_icons = document.querySelector('.navbar_icons') 

toggleBtn.addEventListener('click', ()=>{
    menu.classList.toggle('active')
    navbar_icons.classList.toggle('active')
});