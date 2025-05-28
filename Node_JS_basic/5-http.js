const http = require('http');
const countStudent = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  if (req.url === '/') {
    res.setHeader('Content-Type', 'text/plain');
    res.end('Hello Holberton School!');
  } else if (req.url === '/students') {
    res.setHeader('Content-Type', 'text/plain');

    countStudent(process.argv[2])
      .then((resultado) => {
        res.end(`This is the list of our students\n${resultado}`);
      })
      .catch(() => {
        res.statusCode = 500;
        res.end('Cannot load the database');
      });
  } else {
    res.statusCode = 404;
    res.end('Not found');
  }
});

app.listen(1245);

module.exports = app;
