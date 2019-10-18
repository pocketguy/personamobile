FROM node:10.16.3-alpine

WORKDIR /usr/src/app

COPY package*.json ./

RUN npm install

COPY . .

EXPOSE 80

ENV API_URL=http://backend/
ENV API_URL_BROWSER=https://api.personamobile.ru/

RUN npm run build

CMD npm start -- -H 0.0.0.0 -p 80