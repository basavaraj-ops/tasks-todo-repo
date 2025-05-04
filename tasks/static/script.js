document.addEventListener("DOMContentLoaded", function () {
    const form = document.getElementById('task-form');
    const searchForm = document.getElementById('search-form');
    const taskList = document.getElementById('task-list');

    // Fetch tasks from the API
    function fetchTasks(queryParams = "") {
        fetch(`/tasks/?${queryParams}`)
            .then(response => response.json())
            .then(data => {
                taskList.innerHTML = ''; // Clear the current list
                data.forEach(task => {
                    const li = document.createElement('li');
                    li.textContent = `${task.title} - ${task.description} - ${task.date}`;
                    // Add edit and delete buttons here
                    li.innerHTML += `
                        <button class="edit-btn" data-id="${task.id}">Edit</button>
                        <button class="delete-btn" data-id="${task.id}">Delete</button>
                    `;
                    taskList.appendChild(li);
                });
            })
            .catch(error => console.error('Error fetching tasks:', error));
    }

    // Handle task form submission
    form.addEventListener('submit', function (e) {
        e.preventDefault();

        const title = document.getElementById('title').value;
        const description = document.getElementById('description').value;
        const date = document.getElementById('date').value;

        if (title && description && date) {
            // Send a request to the backend to add a new task
            fetch('/tasks/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ title, description, date })
            })
                .then(response => response.json())
                .then(() => {
                    form.reset();
                    fetchTasks(); // Reload tasks
                })
                .catch(error => console.error('Error adding task:', error));
        }
    });

    // Handle search and sorting form submission
    searchForm.addEventListener('submit', function (e) {
        e.preventDefault();

        const searchTitle = document.getElementById('search-title').value;
        const searchDate = document.getElementById('search-date').value;
        const sortByDate = document.getElementById('sort-by-date').value;

        const queryParams = [
            searchTitle ? `search=${encodeURIComponent(searchTitle)}` : '',
            searchDate ? `search_date=${encodeURIComponent(searchDate)}` : '',
            `sort_by_date=${encodeURIComponent(sortByDate)}`
        ].filter(Boolean).join('&');

        fetchTasks(queryParams); // Fetch tasks with the given filters
    });

    // Fetch tasks on page load
    fetchTasks();
});
