from commands.command_interface import Command
from task_handler import TaskHandler


class EditTaskCommand(Command):
    def __init__(self, task_manager, task, new_description):
        super().__init__(task, task_manager)
        self.old_description = task.getDescription()
        self.new_description = new_description

    def execute(self):
        self._task_manager.EditTaskDescription(self._task.getId(), self.new_description)

    def undo(self):
        self._task_manager.EditTaskDescription(self._task.getId(), self.old_description)