/* eslint-disable indent */
export default function createReportObject(employeesList) {
    return {
        allEmployees: {
            ...employeesList,
        },
        getNumberOfDepartments(empList) {
            return Object.keys(empList).length;
        },
    };
}
