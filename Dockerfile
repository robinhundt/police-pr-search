FROM node:carbon as node

WORKDIR /app

COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn

COPY frontend/ .
RUN yarn build


FROM python:3.6-alpine

WORKDIR /code

RUN apk update \
  && apk add --virtual build-deps gcc python3-dev musl-dev curl 

COPY requirements.txt .

RUN pip install -r requirements.txt && rm -rf /root/.cache
RUN python -m spacy download de

COPY . .
COPY --from=node /app/dist /code/frontend/dist


CMD ["./deploy.sh"]
