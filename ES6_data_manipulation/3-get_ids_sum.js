export default function getStudentIdsSum(students) {
  const sumId = students.reduce((accumulator, currentValue) => accumulator + currentValue.id, 0);
  return sumId;
}
