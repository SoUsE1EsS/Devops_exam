FROM python:3.12-slim

EXPOSE 5000
WORKDIR /usr/app
ENV ENV production
RUN pip install --only-binary :all: greenlet

COPY /app /usr/app/
RUN cd .. \
 && pip install -r requirements.txt \
 && cd app

RUN pip install waitress
CMD waitress-serve --host 0.0.0.0 --port 5000 app:app
