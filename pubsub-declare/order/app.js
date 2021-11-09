const axios = require("axios").default;
const http = require("http");

const daprPort = process.env.DAPR_HTTP_PORT || 3500;
const daprUrl = `http://localhost:${daprPort}/v1.0`;
const port = 3000;
const pubsubName = 'order-pubsub';

const server = http.createServer((request, response) => {
    response.writeHead(200, {
      "Content-Type": "text/html"
    });

    const publishUrl = `${daprUrl}/publish/${pubsubName}/order`;
    axios
      .post(publishUrl, {
        id: "0001",
        name: "sample"
      })
      .then((response) => console.log(response.data))
      .catch(console.log);
    console.log("publish");
    
    response.end("Hello Hiroba!");
});

server.listen(port);
console.log(`The server has started and is listening on port number: ${port}`);
