const http = require("http");
const fs = require("fs");
const URLS = fs.readFileSync("./urls", "utf8").split("\n").filter(Boolean);
const HOST = "https://www.southparkstudios.com";

const server = http.createServer(function (req, res) {
  const randNumber = Math.floor(Math.random() * URLS.length);
  res.writeHead(302, {
    Location: HOST + URLS[randNumber],
  });
  res.end();
});

server.listen(1337, () => console.log("cart.mn"));
