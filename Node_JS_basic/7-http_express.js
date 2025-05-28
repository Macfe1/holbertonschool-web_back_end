const express = require('express');
const countStudent = require('./3-read_file_async');

const app = express();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});

app.get('/students', (req, res) => {
  countStudent(process.argv[2])
    .then((result) => {
      res.send(`This is the list of our students\n ${result}`);
    });
});

app.listen(1245);

module.exports = app;
