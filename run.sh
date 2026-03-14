#!/bin/bash
set -e
cd /root/task
echo "Starting Shopboard infrastructure with docker-compose..."
docker-compose up -d
# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL to accept connections..."
for i in {1..15}; do
  if docker exec shopboard_db pg_isready -U dashboard_admin -d shopboard_db >/dev/null 2>&1; then
    echo "PostgreSQL is ready!"
    break
  else
    sleep 2
  fi
done
# Check FastAPI app status
echo "Checking FastAPI app readiness..."
for i in {1..10}; do
  if curl -s http://localhost:8000/docs >/dev/null; then
    echo "FastAPI app is up and responding."
    exit 0
  else
    sleep 2
  fi
done
echo "Error: FastAPI app did not start as expected. Check logs."
docker-compose logs
exit 1
