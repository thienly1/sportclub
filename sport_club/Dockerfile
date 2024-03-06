FROM python:3-alpine3.19
WORKDIR /sport_club
COPY requirements.txt .

RUN pip install -r requirements.txt
EXPOSE 5000
CMD python3 ./club.py
COPY club.py .

