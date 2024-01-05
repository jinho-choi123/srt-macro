FROM ubuntu:latest
LABEL authors="ball"

ENTRYPOINT ["top", "-b"]