const getStudentIdsSum = (getListStudents) => getListStudents
  .reduce((acc, item) => acc + item.id, 0);
export default getStudentIdsSum;
