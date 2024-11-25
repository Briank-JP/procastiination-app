document.addEventListener('DOMContentLoaded', () => {
    const deleteButtons = document.querySelectorAll('.delete');
    const modal = document.getElementById('deleteModal');
    const confirmButton = document.getElementById('confirmDelete');
    const cancelButton = document.getElementById('cancelDelete');

    let taskToDelete = null;    

    deleteButtons.forEach(button => {
        button.addEventListener('click', (event) => {
            event.preventDefault();
            taskToDelete = button.parentElement.getAttribute('data-id'); // Store task ID
            console.log('Task to delete:', taskToDelete);  // Debug log
            modal.style.display = 'flex';
        });
    });

    cancelButton.addEventListener('click', () => {
        modal.style.display = 'none';
        taskToDelete = null;
    });

    confirmButton.addEventListener('click', () => {
        if (taskToDelete) {
             // Redirect to the delete URL with the task ID
             window.location.href = `/delete/${taskToDelete}/`;
        }
    });
});