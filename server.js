const express = require('express');
const app = express();
const path = require('path');
const http = require('http');

app.use(express.static(path.join(__dirname, 'assets')));

app.get('/', (req, res) => {
    res.sendFile(__dirname + '/index.html');
});

app.get('/menu', (req, res) => {
    res.sendFile(__dirname + '/menu.html');
});

const port = process.env.PORT || 8002;
const server = http.createServer(app);
server.listen(port);
console.log(`Localhost running on port ${port}`);