from dataclasses import dataclass


@dataclass
class UserData:
    chat_id: str
    username: str
    last_updated_dt: str = None
