export default function createReportObject(employeesList) {
  const object = {
    allEmployees: employeesList,
    getNumberOfDepartments() {
      return Object.keys(this.allEmployees).length;
    },
  };
  return object;
}
