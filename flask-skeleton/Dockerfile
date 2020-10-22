FROM python:3.8-alpine

ENV INSTALL_PATH /jackpot
RUN mkdir -p $INSTALL_PATH

WORKDIR $INSTALL_PATH

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

# copy the current directory to a docker container
COPY . .

CMD gunicorn -b 0.0.0.0:8000 --access-logfile - "main.app:create_app()"