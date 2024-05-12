from abc import ABC, abstractmethod

class Command:
    def __init__(self, task, task_manager):
        self._task = task
        self._task_manager = task_manager

    @abstractmethod
    def execute(self):
        pass

    @abstractmethod
    def undo(self):
        pass