FROM python:3.6

# Upgrade PIP
RUN pip install --upgrade pip

# make a local directory
RUN mkdir /application

#ADD . /app
#set the current working directory as app
WORKDIR /application

#move all the current files to the app folder
ADD . .

RUN pip install -r requirements.txt

RUN adduser myuser
USER myuser

#CMD gunicorn --bind 0.0.0.0:$PORT --reload
CMD gunicorn --bind 0.0.0.0:$PORT wsgi