const todoForm = document.querySelector('#todo-form')
const toDoList = document.querySelector('#todo-list')
const toDoInput = todoForm.querySelector("#todo-form input") //todoform 안의 input태그를 찾는법
let toDos =[]
let TODOS_KEY = "Todo"

function saveToDo(){
    localStorage.setItem(TODOS_KEY,JSON.stringify(toDos));
    // JSON.stringify(anything) change the 매개변수 to String Type
}

function paintToDo(newTodo){
    const li = document.createElement("li") // body에 li 태그를 추가 및 선택
    const span = document.createElement("span") // body에 span 태그를 추가 및 선택
    const button = document.createElement('button') //body에 button 태그를 추가 및 선택
    // const HIDDEN = 'hidden'

    function deleteToDo(event){
        // li.classList.add(HIDDEN)
        const lis = event.target.parentElement; // event.target.parentElement요소를 선택후
        console.log(lis);
        lis.remove(); // 그 줄을 지워버림
        
    }

    li.appendChild(span); // li태그 안에 span태그를 집어넣기
    li.appendChild(button) // li태그 안에 button태그를 집어넣기
    button.addEventListener('click',deleteToDo) // click할시 deletetodo 17줄에있는 코드를 실행.

    toDoList.appendChild(li); // toDoList 즉 ul태그 안에 li태그를 집어넣는다.
    

    span.innerText = newTodo;// span태그 안에 텍스트, newtTodo
                             // 즉 매개변수인 newTodo를 집어넣는다
    button.innerText = 'X'; // 버튼의 모양
    saveToDo(); // in line 7 insert the function save todo
    
}




function handleToDoSubmit (tomato){
    event.preventDefault()
    const newTodo = toDoInput.value; // 새로운 값에 복사하기
    toDoInput.value = ""; // 비우는 것 처럼 보이기
    // console.log(newTodo);
    const newTodoObj = {
        text : newTodo,
        id : Date.now()
    }
    toDos.push(newTodoObj); //toDos = Empty array
    paintToDo(newTodo);

}


todoForm.addEventListener('submit',handleToDoSubmit)

const savedToDos = localStorage.getItem(TODOS_KEY); // 일반적인 String형

// function sayHello(item){
//     console.log('this is the turn of ',item)
// } parsedToDos.forEach((item) => console.log('this is the turn of',item))축약

if(savedToDos !== null){
    const parsedToDos = JSON.parse(savedToDos) // String형을 Array로 바꿔준다.
    toDos = parsedToDos; 
    parsedToDos.forEach(paintToDo)// 축약하거나 함수를 쓰거나item) => console.log('this is the turn of',item)
}

//array to want to delete array.filter()
[1,2,3,4].filter(sexyFilter)
console.log([1,2,3,4].filter(sexyFilter))
function sexyFilter(item){
    //should return to true ***
    //and then we get the all array
    //if false we lost the all array
    return item !==3;
}