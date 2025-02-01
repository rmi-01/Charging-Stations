# domain/events/user/user_created_event.py
from datetime import datetime

class CSOperatorLoginEvent:
    def __init__(self, cs_operator_id,username: str, password:str, success: bool = True):
        self.cs_operator_id=cs_operator_id
        self.username = username
        self.password=password
        self.success = success
        self.timestamp = datetime.now()

    def __repr__(self):
        return f"<CSOperatorLoginEvent(user_id={self.user_id}, username={self.username}, password={self.password}, success={self.success})>"

    def as_dict(self):
        return {
            "cs_operator_id":self.cs_operator_id,
            "username": self.username,
            "password":self.password,
            "success": self.success,
            "timestamp": self.timestamp.isoformat()
        }
