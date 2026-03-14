from fastapi import APIRouter, HTTPException, Query
from app.database import get_connection, put_connection
from app.schemas.schemas import StatsResponse, ActivityItem, ActivityListResponse
from typing import List

router = APIRouter(prefix="/api/dashboard")

@router.get("/stats", response_model=StatsResponse)
def get_stats():
    conn = get_connection()
    cur = conn.cursor()
    try:
        users = cur.execute("SELECT * FROM users"); users_count = len(cur.fetchall())
        posts = cur.execute("SELECT * FROM posts"); posts_count = len(cur.fetchall())
        comments = cur.execute("SELECT * FROM comments"); comments_count = len(cur.fetchall())
        sessions = cur.execute("SELECT * FROM sessions"); sessions_count = len(cur.fetchall())
        return {
            "users": users_count,
            "posts": posts_count,
            "comments": comments_count,
            "sessions": sessions_count
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        put_connection(conn)

@router.get("/recent-activity", response_model=ActivityListResponse)
def recent_activity(offset: int = Query(0, ge=0), limit: int = Query(50, ge=1, le=100)):
    conn = get_connection()
    cur = conn.cursor()
    try:
        cur.execute(f"SELECT id, user_id, action, created_at FROM activities ORDER BY created_at DESC, id DESC OFFSET {offset} LIMIT {limit}")
        rows = cur.fetchall()
        activities = [
            {"id": row[0], "user_id": row[1], "action": row[2], "created_at": row[3].isoformat()} for row in rows
        ]
        return {"activities": activities}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cur.close()
        put_connection(conn)
