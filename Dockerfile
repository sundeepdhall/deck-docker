FROM oraclelinux:7-slim

RUN yum-config-manager --enable ol7_developer_EPEL
RUN yum -y install python2-pip
RUN yum -y install python-flask

WORKDIR /app

COPY ./app /app

CMD [ "python", "./deck.py" ]



