@echo off
docker build -t miprograma .
docker run -it --rm miprograma
pause
