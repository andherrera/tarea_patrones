from task import Task
from task_handler import TaskHandler
from commands.add_task_command import AddTaskCommand
from commands.remove_task_command import RemoveTaskCommand
from commands.edit_task_command import EditTaskCommand
from commands.complete_task_command import CompleteTaskCommand
from invoker import Invoker

class Client:
    def __init__(self):
        self.__task_manager = TaskHandler()
        self.__invoker = Invoker()

    def run(self):
        # Create the first task and perform various commands
        task1 = Task(1, "Homework")
        self.__invoker.execute_command(AddTaskCommand(self.__task_manager, task1))
        self.__invoker.execute_command(AddTaskCommand(self.__task_manager, task1))  # This should ideally show an error or be ignored since task1 is already added.
        self.__invoker.execute_command(RemoveTaskCommand(self.__task_manager, task1))
        self.__invoker.undo_last_command()  # Undo remove
        self.__invoker.execute_command(EditTaskCommand(self.__task_manager, task1, "College Homework Design"))
        self.__invoker.undo_last_command()  # Undo edit
        self.__invoker.execute_command(CompleteTaskCommand(self.__task_manager, task1))
        self.__invoker.undo_last_command()  # Undo complete
        self.__invoker.execute_command(CompleteTaskCommand(self.__task_manager, task1))

        # Operations with a second task
        task2 = Task(2, "Report")
        self.__invoker.execute_command(RemoveTaskCommand(self.__task_manager, task2))  # Attempting to remove a non-existing task
        self.__invoker.execute_command(AddTaskCommand(self.__task_manager, task2))

        # List all tasks at the end
        self.__task_manager.ListTasks()

if __name__ == "__main__":
    client = Client()
    client.run()
