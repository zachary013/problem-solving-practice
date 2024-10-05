// Task class
class Task {
    constructor(name, priority = "low") {
        this.name = name;
        this.priority = priority;
        this.completed = false;
    }

    markCompleted() {
        this.completed = true;
    }

    describe() {
        return `${this.name} [Priority: ${this.priority}] - ${this.completed ? 'Completed' : 'Pending'}`;
    }
}

// TaskManager class
class TaskManager {
    constructor() {
        this.tasks = [];
    }

    addTask(task) {
        this.tasks.push(task);
        console.log(`Task "${task.name}" added.`);
    }

    deleteTask(taskName) {
        this.tasks = this.tasks.filter(task => task.name !== taskName);
        console.log(`Task "${taskName}" deleted.`);
    }

    listTasks() {
        if (this.tasks.length === 0) {
            console.log("No tasks available.");
        } else {
            console.log("Task List:");
            this.tasks.forEach(task => console.log(task.describe()));
        }
    }

    // Simulate marking task as completed asynchronously
    markTaskCompleted(taskName) {
        return new Promise((resolve, reject) => {
            const task = this.tasks.find(task => task.name === taskName);

            if (task) {
                setTimeout(() => {
                    task.markCompleted();
                    resolve(`Task "${taskName}" marked as completed.`);
                }, 1000); // Simulate a delay
            } else {
                reject(`Task "${taskName}" not found.`);
            }
        });
    }
}

// Create task manager instance
const taskManager = new TaskManager();

// Add tasks
taskManager.addTask(new Task("Complete JavaScript project", "high"));
taskManager.addTask(new Task("Study for exams", "medium"));
taskManager.addTask(new Task("Buy groceries", "low"));

// List tasks
taskManager.listTasks();

// Simulate marking a task as completed with a promise
taskManager.markTaskCompleted("Complete JavaScript project")
    .then(successMessage => {
        console.log(successMessage);
        taskManager.listTasks();
    })
    .catch(errorMessage => {
        console.error(errorMessage);
    });

// Delete a task after marking it complete
setTimeout(() => {
    taskManager.deleteTask("Buy groceries");
    taskManager.listTasks();
}, 2000);

