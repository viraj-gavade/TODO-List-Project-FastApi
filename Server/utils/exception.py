class CustomException(Exception):
    def __init__(self, name: str, status_code: int):
        self.name = name
        self.detail = f"Custom Exception occurred for task: {name}"
        self.status_code = status_code


class TaskNotFound(CustomException):
    def __init__(self, name: str):
        super().__init__(name, status_code=404)
        self.detail = f"Task not found: {name}"

class TaskAlreadyExists(CustomException):
    def __init__(self, name: str):
        super().__init__(name, status_code=400)
        self.detail = f"Task already exists: {name}"






