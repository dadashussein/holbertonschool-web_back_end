/* eslint-disable no-param-reassign */
export default function updateStudentGradeByCity(objs, city, newGrade) {
  const students = objs.filter((student) => student.city === city);
  // eslint-disable-next-line array-callback-return
  students.map((student) => {
    student.grade = newGrade;
  });
  return students;
}
