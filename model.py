class GreetingResponse:
    def __init__(self, message: str, time: str):
        self.message = message
        self.time = time
    
    def to_dict(self):
        return {
            'message': self.message,
            'time': self.time
        }
