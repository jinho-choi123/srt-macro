# SRT MACRO program

# About
SRT Reservation Macro program

## Prereuisites
**You just need docker installed in your local**

## Getting Started
Run the following command
```bash 
$ git clone git@github.com:jinho-choi123/srt-macro.git

$ cd srt-macro

$ cp .config/.env.example .config/.env 

## fill out .env
$ vim .config/.env

$ docker build . -t jinho-choi123/srt-macro:latest 

$ docker run -it jinho-choi123/srt-macro:latest 

# then select the options you want. To add more stations, goto src/input.py and add more stations to the departures and arrivals list
# currently "수서" and "대전" stations are added...
```

## Built With
- [Python](https://www.python.org/)
- [Docker](https://www.docker.com/)
- [Selenium](https://github.com/SeleniumHQ/selenium)
