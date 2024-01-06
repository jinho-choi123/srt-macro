FROM python:3.10.13

RUN apt-get update

RUN apt-get install curl software-properties-common apt-transport-https ca-certificates -y

RUN curl -fSsL https://dl.google.com/linux/linux_signing_key.pub | gpg --dearmor | tee /usr/share/keyrings/google-chrome.gpg > /dev/null

RUN echo deb [arch=amd64 signed-by=/usr/share/keyrings/google-chrome.gpg] http://dl.google.com/linux/chrome/deb/ stable main | tee /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update

RUN apt-get install google-chrome-stable -y

COPY . /app

# install requirements.txt

WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "main.py"]

