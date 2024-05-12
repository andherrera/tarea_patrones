from commands.command_interface import Command
from task_handler import TaskHandler


class CompleteTaskCommand(Command):
    def __init__(self, task_manager, task):
        super().__init__(task, task_manager)

    def execute(self):
        self._task_manager.SetTaskStatus(self._task.getId(), "Completed")

    def undo(self):
        self._task_manager.SetTaskStatus(self._task.getId(), "In progress")