const images =[
    "0.jpg",
    "1.jpg",
    "2.jpg"
]

const chooseImage = images[Math.floor(Math.random()*images.length)]

const bgImage = document.createElement("img");

bgImage.src = `${chooseImage}` // js상에서만 존재

document.body.appendChild(bgImage) //body태그에 elemnt를 추가할때 사용
// append는 가장 뒤에
// prepend는 가장 앞에
console.log(chooseImage)
console.log(bgImage)