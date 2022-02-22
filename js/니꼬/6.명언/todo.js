const todoForm = document.querySelector('#todo-form')
const toDoList = document.querySelector('#todo-list')
const toDoInput = todoForm.querySelector("#todo-form input") //todoform 안의 input태그를 찾는법
const toDos =[]

function saveToDos(){
    localStorage.setItem('Todo',JSON.stringify(toDos));
}

function paintToDo(newTodo){
    const li = document.createElement("li")
    const span = document.createElement("span")
    const button = document.createElement('button')
    const HIDDEN = 'hidden'


    function deleteToDo(event){
        // li.classList.add(HIDDEN)
        const lis = event.target.parentElement;
        lis.remove();
    }

    
    li.appendChild(span); // li태그 안에 span태그를 집어넣기
    li.appendChild(button)
    button.addEventListener('click',deleteToDo)

    toDoList.appendChild(li);
    console.log(toDoList)

    span.innerText = newTodo;     
    button.innerText = 'X';
    saveToDos();
    
}




function handleToDoSubmit (tomato){
    event.preventDefault()
    const newTodo = toDoInput.value; // 새로운 값에 복사하기
    toDoInput.value = ""; // 비우는 것 처럼 보이기
    // console.log(newTodo);
    toDos.push(newTodo);
    paintToDo(newTodo);

}


todoForm.addEventListener('submit',handleToDoSubmit)