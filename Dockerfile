FROM tiangolo/uwsgi-nginx-flask:python3.7-alpine3.7
RUN apk --update add bash nano

COPY ./portal/requirements.txt requirements.txt

RUN pip install -r requirements.txt

WORKDIR /portal

COPY portal /portal

EXPOSE 5000

CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]