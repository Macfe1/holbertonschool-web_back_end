import fs from 'fs';

function readDatabase(path) {
  return new Promise((resolve, reject) => {
    fs.readFile(path, 'utf8', (err, data) => {
      if (err) {
        reject(new Error('Error'));
        return;
      }
      const lines = data.split('\n');
      const validLines = lines.filter((line) => line.trim() !== '');
      const students = validLines.slice(1);
      const headers = validLines[0].split(',');

      const studentsArray = [];

      students.forEach((line) => {
        const value = line.split(',');
        const student = {};

        headers.forEach((key, index) => {
          student[key] = value[index];
        });
        studentsArray.push(student);
      });

      const countByField = {};

      studentsArray.forEach((student) => {
        const { field } = student;
        if (!countByField[field]) {
          countByField[field] = [];
        }
        countByField[field].push(student.firstname);
      });

      resolve(countByField);
    });
  });
}

export default readDatabase;
