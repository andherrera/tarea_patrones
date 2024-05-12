class TaskHandler:
    def __init__(self):
        self.__tasks = {}

    def AddTask(self, task):
        if task.getId() in self.__tasks:
            print(f"Task with ID {task.getId()} already exists. Please remove it or complete it before attempting to create it again")
        else:
            self.__tasks[task.getId()] = task
            print(f"Added: {task}")

    def EditTaskDescription(self, task_id, new_description):
        task = self.__tasks.get(task_id)
        if task:
            old_description = task.getDescription()
            task.setDescription(new_description) 
            print(f"Edited Task {task_id}: from '{old_description}' to '{new_description}'")
        else:
            print(f"Task {task_id} not found in this task manager for editting description")

    def RemoveTask(self, task_id):
        task = self.__tasks.pop(task_id, None)
        if task:
            print(f"Removed: {task}")
        else: 
            print(f"Task {task_id} not found in this task manager for removal")

    def SetTaskStatus(self, task_id, status):
        task = self.__tasks.get(task_id)
        if task:
            task.setStatus(status) 
            print(f"Setted status task: {task_id} to {status}")

    def ListTasks(self):
        if not self.__tasks:
            print("No tasks available.")
        else:
            print("Listing all tasks in task manager:")
            for key, value in self.__tasks.items():
                print(value) 