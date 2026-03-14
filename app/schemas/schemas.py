from pydantic import BaseModel
from typing import List

class StatsResponse(BaseModel):
    users: int
    posts: int
    comments: int
    sessions: int

class ActivityItem(BaseModel):
    id: int
    user_id: int
    action: str
    created_at: str

class ActivityListResponse(BaseModel):
    activities: List[ActivityItem]
