export default function getStudentsByLocation(objs, city) {
  return objs.filter((student) => student.location === city);
}
