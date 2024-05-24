export default function getListStudentIds(objs) {
  if (!Array.isArray(objs)) {
    return [];
  }
  return objs.map((student) => student.id);
}
