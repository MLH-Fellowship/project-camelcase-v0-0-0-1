#!/bin/bash
cd project-camelcase-v0-0-0-1
git fetch && git reset origin/main --hard
docker compose -f docker-compose.prod.yml down
docker compose -f docker-compose.prod.yml up -d --build

