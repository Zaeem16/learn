let todoList = [{
    name: 'make dinner',
    dueDate: '2022-12-22'
}, {
    name: 'wash dishes',
    dueDate: '2022-12-22'
}];

let todoHistory = localStorage.getItem('todoListHistory');
if (todoHistory !== null) {
    todoList = JSON.parse(todoHistory);
}

renderTodoList();

function renderTodoList() {
    let todoListHTML = '';
  
    for (let i = 0; i < todoList.length; i++) {
        const todoObject = todoList[i];
        const { name, dueDate } = todoObject;
        const html = `
            <div>${name}</div>
            <div>${dueDate}</div>
            <button onclick="deleteTodo(${i})" class="delete-todo-button">Delete</button> 
        `;
        todoListHTML += html;
    }
  
    document.querySelector('.js-todo-list').innerHTML = todoListHTML;
}

function deleteTodo(index) {
    todoList.splice(index, 1);
    localStorage.setItem("todoListHistory", JSON.stringify(todoList));
    renderTodoList();
}

function addTodo() {
    const inputElement = document.querySelector('.js-name-input');
    const name = inputElement.value;

    const dateInputElement = document.querySelector('.js-due-date-input');
    const dueDate = dateInputElement.value;

    // Input validation
    if (!name || !dueDate) {
        alert("Please fill in both fields.");
        return;
    }

    todoList.push({ name, dueDate });
    localStorage.setItem("todoListHistory", JSON.stringify(todoList));
  
    inputElement.value = '';
    dateInputElement.value = ''; // Clear due date input too
  
    renderTodoList();
}