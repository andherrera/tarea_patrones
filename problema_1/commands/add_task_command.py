from commands.command_interface import Command
from task_handler import TaskHandler

class AddTaskCommand(Command):
    def __init__(self, task_manager, task):
        super().__init__(task, task_manager)

    def execute(self):
        self._task_manager.AddTask(self._task)

    def undo(self):
        self._task_manager.RemoveTask(self._task.getId())