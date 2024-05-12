class Task:
    def __init__(self, id, description):
        self.__id = id
        self.__description = description
        self.__status = "In progress"

    def setStatus(self, status):
        self.__status = status
    def getStatus(self):
        return self.__status 
    
    def getId(self):
        return self.__id
    
    def setDescription(self, description):
        self.__description = description
    def getDescription(self):
        return self.__description
        
    def __str__(self):
        return f"Task {self.__id}: {self.__description} [{self.__status}]"