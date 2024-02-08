export default function getListStudentIds(students) {
  if (!Array.isArray(students)) {
    return [];
  }
  const Getid = students.map((students) => students.id);
  return Getid;
}
