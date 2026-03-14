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
        cur.execute("""
            SELECT
                (SELECT COUNT(*) FROM users)    AS users,
                (SELECT COUNT(*) FROM posts)    AS posts,
                (SELECT COUNT(*) FROM comments) AS comments,
                (SELECT COUNT(*) FROM sessions) AS sessions
        """)
        row = cur.fetchone()
        return {"users": row[0], "posts": row[1], "comments": row[2], "sessions": row[3]}
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
        cur.execute(
            "SELECT id, user_id, action, created_at FROM activities ORDER BY created_at DESC, id DESC OFFSET %s LIMIT %s",
            (offset, limit)
        )
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
