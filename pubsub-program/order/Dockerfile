FROM node:lts-alpine3.14

WORKDIR /app
COPY . .
RUN npm install axios
EXPOSE 3000
CMD [ "node", "app.js" ]