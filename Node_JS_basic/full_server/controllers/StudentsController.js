import readDatabase from '../utils';

class StudentsController {
  static getAllStudents(req, res) {
    readDatabase(process.argv[2])
      .then((result) => {
        const sortedFields = Object.keys(result)
          .sort((a, b) => a.toLowerCase().localeCompare(b.toLowerCase()));
        let output = '';
        for (const field of sortedFields) {
          const list = result[field];
          output += `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`;
        }
        res.status(200).send(`This is the list of our students\n${output}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }

  static getAllStudentsByMajor(req, res) {
    const { major } = req.params;

    if (major !== 'CS' && major !== 'SWE') {
      res.status(500).send('Major parameter must be CS or SWE');
    }
    readDatabase(process.argv[2])
      .then((result) => {
        const list = result[major];
        res.status(200).send(`List: ${list.join(', ')}`);
      })
      .catch(() => {
        res.status(500).send('Cannot load the database');
      });
  }
}

export default StudentsController;
