FROM python:3.12-alpine

WORKDIR /usr/app

RUN apk update && apk add bash && apk add curl

COPY . /usr/app

RUN chmod +x start.sh

RUN pip install --no-cache-dir -r requirements.txt

CMD ["./start.sh"]
