const updateStudentGradeByCity = (getListStudents, city, newGrades) => getListStudents
  .filter((item) => item.location === city)
  .map((item) => {
    const gradeInfo = newGrades.find((grade) => grade.studentId === item.id);

    return {
      ...item,
      grade: gradeInfo ? gradeInfo.grade : 'N/A',
    };
  });

export default updateStudentGradeByCity;
