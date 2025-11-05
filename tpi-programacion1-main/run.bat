@echo off
docker build -t miprograma .
docker run --rm miprograma
pause