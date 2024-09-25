#!/bin/bash

# 출력 파일을 저장할 디렉토리를 생성 (존재하지 않을 경우)
mkdir -p trivy_output

# Trivy 실행 및 JSON 형식으로 출력 저장
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock -v $(pwd)/trivy_output:/output aquasec/trivy:latest image wooso --format json --output /output/vulnerabilities.json

