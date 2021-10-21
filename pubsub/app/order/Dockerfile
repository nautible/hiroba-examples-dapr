FROM node:lts-alpine3.14

WORKDIR /usr/src/app
COPY src/ .
RUN npm install axios
EXPOSE 3000
CMD [ "node", "app.js" ]