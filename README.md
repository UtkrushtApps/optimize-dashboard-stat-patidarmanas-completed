# Task Overview
Shopboard is a lightweight analytics dashboard built for a small social network. As user activity has grown, the dashboard’s statistics and recent activity feeds have become noticeably slow to load — especially when users scroll through deeper pages. The database schema currently lacks essential foreign key constraints and indexes, causing performance bottlenecks and increasing the risk of data inconsistency.

## Objectives
- Investigate and improve the response times of the dashboard statistics and recent activity endpoints, particularly under heavy data load or deep pagination
- Analyze the existing database schema and apply appropriate constraints and optimizations to ensure data consistency and faster lookups
- Review query patterns and implement improvements that reduce redundant operations and unnecessary data fetching
- Enhance database connection handling within the API to ensure efficient resource usage and minimal overhead
- Refactor database code to reuse a single DB connection per request rather than per query
- Introduce basic defensive handling around database calls to ensure failures produce clear, correct API responses.

## Database Access
- Host: `<DROPLET_IP>`
- Port: 5432
- Database: shopboard_db
- Username: dashboard_admin
- Password: dash_pwd123

## How to Verify
- Try calling the dashboard stats endpoint with a typical dataset and observe whether the response feels noticeably faster compared to the original behavior.
- Scroll deeper through the recent activity feed and check whether later pages respond more smoothly after your refinements.
- Insert or update sample data to confirm that key relationships between tables are now protected by constraints.
- Use SQL inspection or query analysis tools to see whether the most frequently accessed queries start using the intended indexes more consistently.
- Trigger the endpoints under modest concurrent load to confirm database connections behave predictably and errors surface cleanly without crashing the API.

## Helpful Tips
- The dashboard and activity endpoints work correctly but slow down as the dataset grows, especially when many queries are executed in sequence.
- The stats route performs several independent database lookups, which increases latency and leads to unnecessary repeated work.
- The activity feed queries are not tuned for deeper pagination, so later pages load noticeably slower as more rows accumulate.
- Some essential relationships between users, posts, comments, and sessions are not formally enforced, which can create inconsistencies and make joins less reliable.
- Several frequently queried fields currently lack indexes, which can slow down filtering and ordering operations.
- Reusing a single database connection per request can significantly reduce overhead and simplify resource management.
