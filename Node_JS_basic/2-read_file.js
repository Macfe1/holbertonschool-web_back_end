const fs = require('fs');

function countStudent(path) {
  let data;
  try {
    data = fs.readFileSync(path, 'utf8');
  } catch (error) {
    throw new Error('Cannot load the database');
  }
  const lines = data.split('\n');
  const validLines = lines.filter((line) => line.trim() !== '');
  const students = validLines.slice(1);
  const totalStudents = students.length;
  console.log(`Number of students: ${totalStudents}`);

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

  for (const field in countByField) {
    if (Object.prototype.hasOwnProperty.call(countByField, field)) {
      const list = countByField[field];
      console.log(`Number of students in ${field}: ${list.length}. List: ${list.join(', ')}`);
    }
  }
}
module.exports = countStudent;
