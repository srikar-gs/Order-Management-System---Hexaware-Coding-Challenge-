class OrderNotFound(Exception):
    def __init__(self, message="Order not found"):
        self.message = message
        super().__init__(self.message)
class UnauthorizedAccess(Exception):
    def __init__(self):
        self.message = "Unauthorized access"
        super().__init__(self.message)

    def __str__(self):
        return self.message

class UserNotFoundException(Exception):
    def __init__(self, message):
        self.message = "User not found." 
        super().__init__(self.message)
    def __str__(self):
        return self.message
