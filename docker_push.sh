#!/bin/bash
echo "$DOCKER_PASSWORD" | docker login -u "$DOCKER_USERNAME" --password-stdin
docker tag harshdevl/wisher:latest harshdevl/wisher:1920
docker push harshdevl/wisher:1920
