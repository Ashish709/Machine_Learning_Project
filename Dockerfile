FROM python:3.8
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD ["python3", "app.py"]


#RUN apt update -y && apt install awscli -y



#EXPOSE $PORT
#CMD gunicorn --workers=4 --bind 0.0.0.0:$PORT app:app
