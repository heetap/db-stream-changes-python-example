FROM python:3.6.3

MAINTAINER Dmytro Krupenko <krupenko.d@pdffiller.com>

COPY . /app/
WORKDIR /app/

#Install python dependencies
RUN pip install -r requirements.txt