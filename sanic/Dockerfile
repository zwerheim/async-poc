FROM python:3

EXPOSE 8000

VOLUME /opt/service

WORKDIR /opt/service

COPY ./service /opt/service

COPY requirements.txt /tmp/requirements.txt

RUN pip install --no-cache-dir -U -r /tmp/requirements.txt

CMD ["python", "app.py"]
