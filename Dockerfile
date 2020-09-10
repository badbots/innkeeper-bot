FROM python:3.8-buster

RUN adduser --disabled-password innkeeperbot

WORKDIR /home/innkeeperbot

COPY app.py ./
COPY requirements.txt ./
COPY modules modules
COPY voice_lines voice_lines
RUN apt-get -y update \
    && apt-get -y upgrade \
    && apt-get install -y ffmpeg
RUN pip install -r requirements.txt

RUN chown -R innkeeperbot:innkeeperbot ./
USER innkeeperbot

CMD ["python", "app.py"]