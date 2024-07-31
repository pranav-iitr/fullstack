FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV DJANGO_CONFIGURATION=Dev

RUN mkdir /usr/itx
WORKDIR /usr/itx

COPY ./requirements.txt /requirements.txt
RUN pip install -r /requirements.txt
RUN pip install --upgrade 'sentry-sdk[django]'


COPY . .

CMD ["sh", "-c", "export PYTHONPATH=/usr/itx;export DJANGO_CONFIGURATION=Dev; python manage.py collectstatic --no-input;python manage.py makemigrations;python manage.py migrate;gunicorn Backend.wsgi:application -b 0.0.0.0:9556 --timeout 60000 "]