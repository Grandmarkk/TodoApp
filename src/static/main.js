/**
 * @description This file contains the JavaScript code for the todo app.
 * It handles the creation, updating, and deletion of todo items.
 * It also fetches the todo items from the server and displays them on the page.
 */

/**
 * @description This function fetches the todo items from the server and displays them on the page.
 */
let getTodoItems = () => {

    // fetch the todo items from the server
    let items = document.getElementById('todos');
    let itemsHTML = ''

    fetch("/api/todo")
        .then((response) => response.json())
        .then((data) => {
            for (const item of data) {
                // create a list item for each todo item
                itemsHTML += `
                    <li
                        class="list-group-item d-flex justify-content-between align-items-center
                                border-start-0 border-top-0 border-end-0 border-bottom rounded-0 mb-2">
                        <div class="d-flex align-items-center" id="item-${item.id}" data-value="${item.task}">
                            ${item.task}
                        </div>
                        <div class="float-end">
                            <i class="fas fa-pen text-primary" style="margin-right: 30px" data-mdb-toggle="modal"
                             data-mdb-target="#exampleModal" onclick='updateTodoItem(${item.id})'></i>
                            <i class="fas fa-times text-primary" onclick='deleteTodoItem(${item.id})'></i>
                        </div>
                    </li>
                `
            }
            items.innerHTML = itemsHTML;
        })
        .catch(console.error);
}

getTodoItems();

/**
 * @description create a new todo item
 * @param {Event} e - the event object
 * @returns {void} 
 */
let createTodoItem = (e) => {

    e.preventDefault();
    todoTask = document.getElementById('todoTask').value;
    const data = { task: todoTask };
    // send the data to the server
    fetch('/api/todo', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    })
        .then((response) => response.json())
        .then((data) => {
            getTodoItems();
        })
        .catch((error) => {
            console.error('Error:', error);
        });

    // reset form
    document.getElementById('todo-from').reset();
}

/**
 * @description update a todo item
 * @param {number} id - the id of the todo item to update
 */
let updateTodoItem = (id) => {
    let modalInput = document.getElementById('todo-text');
    let updateTodoBtn = document.getElementById("update-todo")
    let todoItem = document.getElementById(`item-${id}`).getAttribute('data-value');
    modalInput.value = todoItem
    // set the value of the input field to the current todo item
    updateTodoBtn.addEventListener('click', () => {
        const data = { task: modalInput.value };
        fetch(`/api/todo/${id}`, {
            method: 'PATCH',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(data),
        })
            .then((response) => response.json())
            .then((data) => {
                getTodoItems();
            })
            .catch((error) => {
                console.error('Error:', error);
            });
    }, { once: true })
}

// delete a todo item
let deleteTodoItem = (id) => {
    // send the request to the server
    fetch(`/api/todo/${id}`, {
        method: 'DELETE',
    })
        .then((response) => response.json())
        .then((data) => {
            getTodoItems();
        })
        .catch((error) => {
            console.error('Error:', error);
        });
}