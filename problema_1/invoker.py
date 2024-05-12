class Invoker:
    def __init__(self):
        self.__history = []

    def execute_command(self, command):
        command.execute()
        self.__history.append(command)

    def undo_last_command(self):
        if self.__history:
            command = self.__history.pop()
            command.undo()