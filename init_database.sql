-- Inefficient base schema, no indexes/constraints
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(50),
    status VARCHAR(20),
    created_at TIMESTAMP
);

CREATE TABLE posts (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    status VARCHAR(20),
    content TEXT,
    created_at TIMESTAMP
);

CREATE TABLE comments (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    post_id INTEGER,
    status VARCHAR(20),
    content TEXT,
    created_at TIMESTAMP
);

CREATE TABLE sessions (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    is_active BOOLEAN,
    created_at TIMESTAMP
);

CREATE TABLE activities (
    id SERIAL PRIMARY KEY,
    user_id INTEGER,
    action VARCHAR(255),
    created_at TIMESTAMP
);

-- Minimal sample data
INSERT INTO users (username, status, created_at) VALUES ('alice', 'active', NOW());
INSERT INTO users (username, status, created_at) VALUES ('bob', 'active', NOW());
INSERT INTO posts (user_id, status, content, created_at) VALUES (1, 'published', 'Hello World', NOW());
INSERT INTO posts (user_id, status, content, created_at) VALUES (2, 'draft', 'Draft Post', NOW());
INSERT INTO comments (user_id, post_id, status, content, created_at) VALUES (1, 1, 'approved', 'Nice post!', NOW());
INSERT INTO comments (user_id, post_id, status, content, created_at) VALUES (2, 1, 'pending', 'Needs review.', NOW());
INSERT INTO sessions (user_id, is_active, created_at) VALUES (1, true, NOW());
INSERT INTO sessions (user_id, is_active, created_at) VALUES (2, false, NOW());
INSERT INTO activities (user_id, action, created_at) VALUES (1, 'created post', NOW());
INSERT INTO activities (user_id, action, created_at) VALUES (2, 'commented', NOW());
-- Artificially add 1500 activities for pagination test
DO $$
DECLARE rec INT;
BEGIN
    FOR rec IN 3..1503 LOOP
        INSERT INTO users (username, status, created_at) VALUES ('user' || rec, 'active', NOW());
        INSERT INTO activities (user_id, action, created_at) VALUES (rec, 'activity #' || rec, NOW() - INTERVAL '1 minute' * rec);
    END LOOP;
END$$;
