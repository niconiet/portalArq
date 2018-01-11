FROM python:3.5

ENV PYTHONUNBUFFERED 1
ADD . /

WORKDIR /src/portal

#RUN apt-get update -y && apt-get install apache2 -y && apt-get install apache2-dev -y && pip3 install Django==1.10 && pip3 install -r /src/requirements.txt && apt-get install python3-lxml -y && python3 manage.py collectstatic --noinput
#RUN pip3 install lxml
EXPOSE 80
#www-data permission

#CMD ["python3", "manage.py", "runmodwsgi", "--port=80", "--user=www-data", "--group=www-data"]

RUN pip3 install Django==1.10 && pip3 install -r /src/requirements.txt && python3 manage.py collectstatic --noinput

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
