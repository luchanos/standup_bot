from dataclasses import dataclass, field
from typing import List


@dataclass
class UserData:
    chat_id: str
    username: str
    last_updated_dt: str = None
    total_programming_time: List = field(default_factory=lambda: [])
