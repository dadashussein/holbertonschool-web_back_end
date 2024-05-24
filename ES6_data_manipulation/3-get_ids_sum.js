/* eslint-disable array-callback-return */
export default function getStudentIdsSum(objs) {
  const uids = [];
  objs.map((student) => {
    uids.push(student.id);
  });

  return uids.reduce((acc, cal) => acc + cal);
}
