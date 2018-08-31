FROM node:carbon as node

WORKDIR /app

COPY frontend/package.json .
COPY frontend/yarn.lock .
RUN yarn

COPY frontend/ .
RUN yarn build


FROM python:3.6-alpine

WORKDIR /code

COPY requirements.txt .

RUN pip install -r requirements.txt && rm -rf /root/.cache
RUN python -m spacy download de

COPY . .
COPY --from=node /app/dist /code/frontend/dist


CMD ["./deploy.sh"]
